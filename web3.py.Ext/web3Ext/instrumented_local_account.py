from typing import Mapping, NamedTuple
import warnings

from eth_account.signers.base import (
    BaseAccount,
)
from eth_account._utils.signing import (
    sign_transaction_dict,
    serializable_unsigned_transaction_from_dict,
    sign_transaction_hash,
    encode_transaction,
    Transaction,
    TypedTransaction,
    UnsignedTransaction,
)
from eth_utils.curried import (
    keccak,
)
from eth_account.datastructures import (
    SignedTransaction,
)
from hexbytes import (
    HexBytes,
)
from cytoolz import (
    dissoc,
)
from eth_utils.curried import (
    hexstr_if_str,
    text_if_str,
    to_int,
)

# It can has the decoupled keypair to support klaytn abstract account
class AbstractLocalAccount(BaseAccount):
    r"""
    A collection of convenience methods to sign and encrypt, with an
    embedded private key.

    :var bytes key: the 32-byte private key data

    .. code-block:: python

        >>> my_local_account.address
        "0xF0109fC8DF283027b6285cc889F5aA624EaC1F55"
        >>> my_local_account.key
        b"\x01\x23..."

    You can also get the private key by casting the account to :class:`bytes`:

    .. code-block:: python

        >>> bytes(my_local_account)
        b"\\x01\\x23..."
    """

    def __init__(self, *args):
        if len(args) == 2:
            key, account = args[0], args[1]
            self._publicapi = account
            self._address = key.public_key.to_checksum_address()
            key_raw = key.to_bytes()
            self._private_key = key_raw
            self._key_obj = key
        elif len(args) == 3:
            address, key, account = args[0], args[1], args[2]
            self._publicapi = account
            self._address = address
            key_raw = key.to_bytes()
            self._private_key = key_raw
            self._key_obj = key
            self.public_key = self._key_obj.public_key.to_checksum_address()

    @property
    def address(self):
        return self._address

    @property
    def key(self):
        """
        Get the private key.
        """
        return self._private_key

    def encrypt(self, password, kdf=None, iterations=None):
        """
        Generate a string with the encrypted key.

        This uses the same structure as in
        :meth:`~eth_account.account.Account.encrypt`, but without a
        private key argument.
        """
        return self._publicapi.encrypt(
            self.key, password, kdf=kdf, iterations=iterations
        )

    def signHash(self, message_hash):
        return self._publicapi.signHash(
            message_hash,
            private_key=self.key,
        )

    def sign_message(self, signable_message):
        """
        Generate a string with the encrypted key.

        This uses the same structure as in
        :meth:`~eth_account.account.Account.sign_message`, but without a
        private key argument.
        """
        return self._publicapi.sign_message(signable_message, private_key=self.key)

    def signTransaction(self, transaction_dict):
        warnings.warn(
            "signTransaction is deprecated in favor of sign_transaction",
            category=DeprecationWarning,
        )
        return self.sign_transaction(transaction_dict)

    def sign_transaction(self, transaction_dict):
        return self._publicapi.sign_transaction(transaction_dict, self.key)

    def __bytes__(self):
        return self.key


class KlaytnSignedTransaction(NamedTuple):
    rawTransaction: HexBytes
    hash: HexBytes
    senderTxHash: HexBytes
    r: int
    s: int
    v: int

    def __getitem__(self, index):
        try:
            return tuple.__getitem__(self, index)
        except TypeError:
            return getattr(self, index)


def sign_transaction(self, transaction_dict, private_key):
    if not isinstance(transaction_dict, Mapping):
        raise TypeError("transaction_dict must be dict-like, got %r" % transaction_dict)

    account = self.from_key(private_key)

    if "type" in transaction_dict and hexstr_if_str(to_int, transaction_dict["type"]) < 8:
        # allow from field, *only* if it matches the private key
        if "from" in transaction_dict:
            if transaction_dict["from"] == account.address:
                sanitized_transaction = dissoc(transaction_dict, "from")
            else:
                raise TypeError(
                    "from field must match key's %s, but it was %s"
                    % (
                        account.address,
                        transaction_dict["from"],
                    )
                )
        else:
            sanitized_transaction = transaction_dict

        # sign transaction
        v, r, s, encoded_transaction = sign_transaction_dict(account._key_obj, sanitized_transaction)
        transaction_hash = keccak(encoded_transaction)
        return SignedTransaction(
            rawTransaction=HexBytes(encoded_transaction),
            hash=HexBytes(transaction_hash),
            r=r,
            s=s,
            v=v,
        )
    else:
        v, r, s, encoded_transaction, transaction_hash, senderTxHash = sign_klaytn_transaction_dict(account._key_obj, transaction_dict)
        return KlaytnSignedTransaction(
            rawTransaction=HexBytes(encoded_transaction),
            hash=HexBytes(transaction_hash),
            senderTxHash=HexBytes(senderTxHash),
            r=r,
            s=s,
            v=v,
        )

def sign_klaytn_transaction_dict(eth_key, transaction_dict):
    # generate RLP-serializable transaction, with defaults filled
    unsigned_transaction = serializable_unsigned_transaction_from_dict(transaction_dict)
    if not isinstance(unsigned_transaction, TypedTransaction):
        raise TypeError("given transaction type is expected: TypedTransaction, but %s", type(unsigned_transaction))
    
    transaction_hash = unsigned_transaction.hash()
    chain_id = text_if_str(to_int, transaction_dict["chainId"])
    (v, r, s) = sign_transaction_hash(eth_key, transaction_hash, chain_id)
    encoded_transaction = encode_transaction(unsigned_transaction, vrs=(v,r,s))

    return v, r, s, encoded_transaction, transaction_hash, transaction_hash