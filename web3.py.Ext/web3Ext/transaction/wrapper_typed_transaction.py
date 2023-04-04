from typing import (
    Any,
    Dict,
    Union,
)
from cytoolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)
from .value_transfer_transaction import ValueTransferTransaction
from eth_account._utils.typed_transactions import (
    TypedTransaction,
    _TypedTransactionImplementation,
    AccessListTransaction,
    DynamicFeeTransaction,
    HexBytes,
    set_transaction_type_if_needed,
    is_int_or_prefixed_hexstr,
)
from eth_utils.curried import (
    hexstr_if_str,
    to_int,
    to_bytes,
)
from eth_account._utils.transaction_utils import (
    set_transaction_type_if_needed,
)
from eth_account._utils.validation import (
    is_int_or_prefixed_hexstr,
)

# Klaytn wrapped typed transaction
"""
Represents a Typed Transaction as per EIP-2718.
The currently supported Transaction Types are:
    * Klaytn Extended LegacyTransactionTransaction
    * Klaytn Extended ValueTransferTransaction
    * Klaytn Extended FeeDelegatedValueTransferTransaction
    * Klaytn Extended FeeDelegatedValueTransferWithRatioTransaction
    * Klaytn Extended FeeDelegatedValueTransferMemoWithRatioTransaction
    * Klaytn Extended AccountUpdateTransaction
    * Klaytn Extended FeeDelegatedAccountUpdateTransaction
    * Klaytn Extended FeeDelegatedAccountUpdateWithRatioTransaction
    * Klaytn Extended SmartContractDeployTransaction
    * Klaytn Extended FeeDelegatedSmartContractDeployTransaction
    * Klaytn Extended FeeDelegatedSmartContractDeployWithRatioTransaction
    * Klaytn Extended SmartContractExecutionTransaction
    * Klaytn Extended FeeDelegatedSmartContractExecutionTransaction
    * Klaytn Extended FeeDelegatedSmartContractExecutionWithRatioTransaction
    * Klaytn Extended CancelTransaction
    * Klaytn Extended FeeDelegatedCancelTransaction
    * Klaytn Extended FeeDelegatedCancelWithRatioTransaction
    * Klaytn Extended ChainDataAnchoringTransaction
    * Klaytn Extended FeeDelegatedChainDataAnchoringTransaction
    * Klaytn Extended FeeDelegatedChainDataAnchoringWithRatioTransaction
    * Klaytn Extended EthereumAccessListTransaction
    * Klaytn Extended EthereumDynamicFeeTransaction
    
    * EIP-2930's AccessListTransaction : is translated as Klaytn Extended EIP-2930
    * EIP-1559's DynamicFeeTransaction : is translated as Klaytn Extended EIP-1559
"""
def from_dict(cls, dictionary: Dict[str, Any]) -> "TypedTransaction":
    """
    Builds a TypedTransaction from a dictionary.
    Verifies the dictionary is well formed.
    """
    dictionary = set_transaction_type_if_needed(dictionary)
    if not ("type" in dictionary and is_int_or_prefixed_hexstr(dictionary["type"])):
        raise ValueError("missing or incorrect transaction type")
    # Switch on the transaction type to choose the correct constructor.
    transaction_type = pipe(dictionary["type"], hexstr_if_str(to_int))
    klaytn_transaction_type = dictionary["type"]
    transaction: Any
    if transaction_type == AccessListTransaction.transaction_type:
        transaction = AccessListTransaction
    elif transaction_type == DynamicFeeTransaction.transaction_type:
        transaction = DynamicFeeTransaction
    elif transaction_type == ValueTransferTransaction.transaction_type:
        transaction = ValueTransferTransaction
    else:
        raise TypeError("Unknown Transaction type: %s" % transaction_type)
    return cls(
        transaction_type=transaction_type,
        transaction=transaction.from_dict(dictionary),
    )

def from_bytes(cls, encoded_transaction: HexBytes) -> "TypedTransaction":
    """Builds a TypedTransaction from a signed encoded transaction."""
    if not isinstance(encoded_transaction, HexBytes):
        raise TypeError("expected Hexbytes, got %s" % type(encoded_transaction))
    if not (len(encoded_transaction) > 0 and encoded_transaction[0] <= 0x7F):
        raise ValueError("unexpected input")
    transaction: Union["DynamicFeeTransaction", "AccessListTransaction"]
    if encoded_transaction[0] == AccessListTransaction.transaction_type:
        transaction_type = AccessListTransaction.transaction_type
        transaction = AccessListTransaction.from_bytes(encoded_transaction)
    elif encoded_transaction[0] == DynamicFeeTransaction.transaction_type:
        transaction_type = DynamicFeeTransaction.transaction_type
        transaction = DynamicFeeTransaction.from_bytes(encoded_transaction)
    elif encoded_transaction[0] == ValueTransferTransaction.transaction_type:
        transaction_type = ValueTransferTransaction.transaction_type
        transaction = ValueTransferTransaction.from_bytes(encoded_transaction)
    else:
        # The only known transaction types should be explicit if/elif branches.
        raise TypeError(
            "typed transaction has unknown type: %s" % encoded_transaction[0]
        )
    return cls(
        transaction_type=transaction_type,
        transaction=transaction,
    )
