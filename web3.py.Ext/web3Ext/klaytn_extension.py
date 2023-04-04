import types
from eth_account import Account
from eth_account._utils import legacy_transactions
from eth_account._utils.typed_transactions import (
    TypedTransaction,
)
from transaction.wrapper_typed_transaction import (
    from_dict,
    from_bytes,
    encode,
    __init__,
)
from instrumented_local_account import (
    AbstractLocalAccount,
    sign_transaction,
    sign_transaction_dict,
)

ALLOWED_TRANSACTION_KEYS = {
    "nonce",
    "gasPrice",
    "gas",
    "to",
    "value",
    "data",
    "from",
    # set chainId to None if you want a transaction that can be replayed across networks
    "chainId",
    "typeInt",
}

# def init_from_key_pair(self, *args):
#     if len(args) == 2:
#         key, account = args[0], args[1]
#         self._publicapi = account
#         self._address = key.public_key.to_checksum_address()
#         key_raw = key.to_bytes()
#         self._private_key = key_raw
#         self._key_obj = key
#     elif len(args) == 3:
#         address, key, account = args[0], args[1], args[2]
#         self._publicapi = account
#         self._address = address
#         key_raw = key.to_bytes()
#         self._private_key = key_raw
#         self._key_obj = key
#         self.public_key = self._key_obj.public_key.to_checksum_address()

def from_key_pair(self, address, key):
    key = self._parsePrivateKey(key)
    return AbstractLocalAccount(address, key, self)

# account
# LocalAccount.__init__ = types.MethodType(init_from_key_pair, LocalAccount)
Account.from_key_pair = types.MethodType(from_key_pair, Account)
Account.sign_transaction = types.MethodType(sign_transaction, Account)
Account.sign_transaction_dict = types.MethodType(sign_transaction_dict, Account)

# transaction
TypedTransaction.from_dict = types.MethodType(from_dict, TypedTransaction)
TypedTransaction.from_bytes = types.MethodType(from_bytes, TypedTransaction)
TypedTransaction.encode = types.MethodType(encode, TypedTransaction)
TypedTransaction.__init__ = types.MethodType(__init__, TypedTransaction)
legacy_transactions.ALLOWED_TRANSACTION_KEYS = ALLOWED_TRANSACTION_KEYS