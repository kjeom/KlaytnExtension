import types
from eth_account import Account
from eth_account._utils.typed_transactions import (
    TypedTransaction,
)
from transaction.wrapper_typed_transaction import (
    from_dict,
    from_bytes,
    _klay_send_raw_transaction,
)
from klaytn_account.instrumented_local_account import (
    AbstractLocalAccount,
    klaytn_extended_sign_transaction,
    klaytn_extended_sign_transaction_as_feepayer,
    klaytn_extended_recover_transaction_as_feepayer,
    klaytn_extended_decode_transaction,
)
from web3.eth.eth import Eth
from web3._utils.method_formatters import ABI_REQUEST_FORMATTERS
from transaction.extended_transaction_utils import (
    from_peb,
    to_peb,
)
from web3.main import BaseWeb3


def from_key_pair(self, address, key):
    key = self._parsePrivateKey(key)
    return AbstractLocalAccount(address, key, self)

# account
Account.from_key_pair = types.MethodType(from_key_pair, Account)
Account.sign_transaction = types.MethodType(klaytn_extended_sign_transaction, Account)
Account.sign_transaction_as_feepayer = types.MethodType(klaytn_extended_sign_transaction_as_feepayer, Account)
Account.recover_transaction_as_feepayer = types.MethodType(klaytn_extended_recover_transaction_as_feepayer, Account)
Account.decode_transaction = types.MethodType(klaytn_extended_decode_transaction, Account)

# transaction
TypedTransaction.from_dict = types.MethodType(from_dict, TypedTransaction)
TypedTransaction.from_bytes = types.MethodType(from_bytes, TypedTransaction)
Eth._send_raw_transaction = _klay_send_raw_transaction
ABI_REQUEST_FORMATTERS['klay_sendRawTransaction'] = ABI_REQUEST_FORMATTERS['eth_sendRawTransaction']

# util
# BaseWeb3.to_peb = types.MethodType(to_peb, BaseWeb3)
# BaseWeb3.from_peb = types.MethodType(from_peb, BaseWeb3)