import copy

TX_TYPE_LEGACY_TRANSACTION = 0x0
TX_TYPE_VALUE_TRANSFER = 0x08
TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER = 0x09
TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_WITH_RATIO = 0x0a
TX_TYPE_VALUE_TRANSFER_MEMO = 0x10
TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO = 0x11
TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO_WITH_RATIO = 0x12
TX_TYPE_ACCOUNT_UPDATE = 0x20
TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE = 0x21
TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE_WITH_RATIO = 0x22
TX_TYPE_SMART_CONTRACT_DEPLOY = 0x28
TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY = 0x29
TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY_WITH_RATIO = 0x2a
TX_TYPE_SMART_CONTRACT_EXECUTION = 0x30
TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION = 0x31
TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION_WITH_RATIO = 0x32
TX_TYPE_CANCEL = 0x38
TX_TYPE_FEE_DELEGATED_CANCEL = 0x39
TX_TYPE_FEE_DELEGATED_CANCEL_WITH_RATIO = 0x3a
TX_TYPE_CHAIN_DATA_ANCHORING = 0x48
TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING = 0x49
TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING_WITH_RATIO = 0x4a
TX_TYPE_ETHEREUM_ACCESS_LIST = 0x7801
TX_TYPE_ETHEREUM_DYNAMIC_FEE = 0x7802

TX_TYPE_VALUE_TO_HEX_STRING = {
    TX_TYPE_LEGACY_TRANSACTION : '0x0',
    TX_TYPE_VALUE_TRANSFER : '0x08',
    TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER : '0x09',
    TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_WITH_RATIO : '0x0a',
    TX_TYPE_VALUE_TRANSFER_MEMO : '0x10',
    TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO : '0x11',
    TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO_WITH_RATIO : '0x12',
    TX_TYPE_ACCOUNT_UPDATE : '0x20',
    TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE : '0x21',
    TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE_WITH_RATIO : '0x22',
    TX_TYPE_SMART_CONTRACT_DEPLOY : '0x28',
    TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY : '0x29',
    TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY_WITH_RATIO : '0x2a',
    TX_TYPE_SMART_CONTRACT_EXECUTION : '0x30',
    TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION : '0x31',
    TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION_WITH_RATIO : '0x32',
    TX_TYPE_CANCEL : '0x38',
    TX_TYPE_FEE_DELEGATED_CANCEL : '0x39',
    TX_TYPE_FEE_DELEGATED_CANCEL_WITH_RATIO : '0x3a',
    TX_TYPE_CHAIN_DATA_ANCHORING : '0x48',
    TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING : '0x49',
    TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING_WITH_RATIO : '0x4a',
    TX_TYPE_ETHEREUM_ACCESS_LIST : '0x7801',
    TX_TYPE_ETHEREUM_DYNAMIC_FEE : '0x7802',
}

TX_TYPE_HEX_TO_STRING = {
    '': 'TxTypeLegacyTransaction',

    '0x08': 'TxTypeValueTransfer',
    '0x09': 'TxTypeFeeDelegatedValueTransfer',
    '0x0a': 'TxTypeFeeDelegatedValueTransferWithRatio',

    '0x10': 'TxTypeValueTransferMemo',
    '0x11': 'TxTypeFeeDelegatedValueTransferMemo',
    '0x12': 'TxTypeFeeDelegatedValueTransferMemoWithRatio',

    '0x20': 'TxTypeAccountUpdate',
    '0x21': 'TxTypeFeeDelegatedAccountUpdate',
    '0x22': 'TxTypeFeeDelegatedAccountUpdateWithRatio',

    '0x28': 'TxTypeSmartContractDeploy',
    '0x29': 'TxTypeFeeDelegatedSmartContractDeploy',
    '0x2a': 'TxTypeFeeDelegatedSmartContractDeployWithRatio',

    '0x30': 'TxTypeSmartContractExecution',
    '0x31': 'TxTypeFeeDelegatedSmartContractExecution',
    '0x32': 'TxTypeFeeDelegatedSmartContractExecutionWithRatio',

    '0x38': 'TxTypeCancel',
    '0x39': 'TxTypeFeeDelegatedCancel',
    '0x3a': 'TxTypeFeeDelegatedCancelWithRatio',

    '0x48': 'TxTypeChainDataAnchoring',
    '0x49': 'TxTypeFeeDelegatedChainDataAnchoring',
    '0x4a': 'TxTypeFeeDelegatedChainDataAnchoringWithRatio',

    '0x7801': 'TxTypeEthereumAccessList',
    '0x7802': 'TxTypeEthereumDynamicFee',
}

TX_TYPE_STRING_TO_HEX = {
    'TxTypeLegacyTransaction':'',

    'TxTypeValueTransfer':'0x08',
    'TxTypeFeeDelegatedValueTransfer':'0x09',
    'TxTypeFeeDelegatedValueTransferWithRatio':'0x0a',

    'TxTypeValueTransferMemo':'0x10',
    'TxTypeFeeDelegatedValueTransferMemo':'0x11',
    'TxTypeFeeDelegatedValueTransferMemoWithRatio':'0x12',

    'TxTypeAccountUpdate':'0x20',
    'TxTypeFeeDelegatedAccountUpdate':'0x21',
    'TxTypeFeeDelegatedAccountUpdateWithRatio':'0x22',

    'TxTypeSmartContractDeploy':'0x28',
    'TxTypeFeeDelegatedSmartContractDeploy':'0x29',
    'TxTypeFeeDelegatedSmartContractDeployWithRatio':'0x2a',

    'TxTypeSmartContractExecution':'0x30',
    'TxTypeFeeDelegatedSmartContractExecution':'0x31',
    'TxTypeFeeDelegatedSmartContractExecutionWithRatio':'0x32',

    'TxTypeCancel':'0x38',
    'TxTypeFeeDelegatedCancel':'0x39',
    'TxTypeFeeDelegatedCancelWithRatio':'0x3a',

    'TxTypeChainDataAnchoring':'0x48',
    'TxTypeFeeDelegatedChainDataAnchoring':'0x49',
    'TxTypeFeeDelegatedChainDataAnchoringWithRatio':'0x4a',

    'TxTypeEthereumAccessList':'0x7801',
    'TxTypeEthereumDynamicFee':'0x7802',
}

ALLOWED_TRANSACTION_KEYS = {
    "nonce",
    "gasPrice",
    "gas",
    "to",
    "value",
    "data",
    'from',
    # set chainId to None if you want a transaction that can be replayed across networks
    "chainId",
}

base_tx = {
    'from':None,
    'to':None,
    'gas':90000,
    'gasPrice':None,
    'nonce':None
}

def empty_tx(tx_type):
    account_update_tx = copy.deepcopy(base_tx)
    if tx_type == TX_TYPE_LEGACY_TRANSACTION:
        pass
    elif tx_type == TX_TYPE_VALUE_TRANSFER:
        account_update_tx['type'] = TX_TYPE_VALUE_TRANSFER
        # account_update_tx['type'] = TX_TYPE_HEX_TO_STRING['TxTypeValueTransfer']
        # account_update_tx['type'] = TX_TYPE_VALUE_TO_HEX_STRING[TX_TYPE_VALUE_TRANSFER]
        account_update_tx['value'] = None
        return account_update_tx
    elif tx_type == TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_VALUE_TRANSFER_MEMO:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_VALUE_TRANSFER_MEMO_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_ACCOUNT_UPDATE:
        account_update_tx['type'] = TX_TYPE_ACCOUNT_UPDATE
        # account_update_tx['type'] = TX_TYPE_HEX_TO_STRING['TxTypeAccountUpdate']
        # account_update_tx['type'] = TX_TYPE_VALUE_TO_HEX_STRING[TX_TYPE_ACCOUNT_UPDATE]
        account_update_tx['key'] = None
        return account_update_tx
    elif tx_type == TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_ACCOUNT_UPDATE_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_SMART_CONTRACT_DEPLOY:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_DEPLOY_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_SMART_CONTRACT_EXECUTION:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_SMART_CONTRACT_EXECUTION_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_CANCEL:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_CANCEL:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_CANCEL_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_CHAIN_DATA_ANCHORING:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING:
        pass
    elif tx_type == TX_TYPE_FEE_DELEGATED_CHAIN_DATA_ANCHORING_WITH_RATIO:
        pass
    elif tx_type == TX_TYPE_ETHEREUM_ACCESS_LIST:
        pass
    elif tx_type == TX_TYPE_ETHEREUM_DYNAMIC_FEE:
        pass

def fill_transaction(transaction):
    if isinstance(transaction, dict):
        keys = transaction.keys()
        if "gasPrice" in keys and transaction['gasPrice'] is None:
            # TODO: set the getGasPrice() API result, but just 30ston now.
            transaction['gasPrice'] = 30000000000
        if "nonce" in keys and transaction['nonce'] is None:
            # TODO: set the getTransactionCount() API result, but just 0 now.
            transaction['nonce'] = 0

    return transaction



























