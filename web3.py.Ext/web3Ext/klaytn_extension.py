import types
from eth_account import Account
from eth_account._utils.typed_transactions import (
    TypedTransaction,
)
from transaction.wrapper_typed_transaction import (
    from_dict,
    from_bytes,
)
from instrumented_local_account import (
    AbstractLocalAccount,
    klaytn_sign_transaction,
    # sign_transaction_dict,
)

def from_key_pair(self, address, key):
    key = self._parsePrivateKey(key)
    return AbstractLocalAccount(address, key, self)

# account
Account.from_key_pair = types.MethodType(from_key_pair, Account)
Account.sign_transaction = types.MethodType(klaytn_sign_transaction, Account)
# Account.sign_transaction_dict = types.MethodType(sign_transaction_dict, Account)

# transaction
TypedTransaction.from_dict = types.MethodType(from_dict, TypedTransaction)
TypedTransaction.from_bytes = types.MethodType(from_bytes, TypedTransaction)