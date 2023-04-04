import code

import klaytn_extension
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils.curried import to_hex, to_bytes
from transaction import transaction
import copy

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8551'))
def web3_integration_test():
    # acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
    acc = Account.from_key_pair(
        '0x912638E1C201C3e1fFAc14bb720cC4944e7A6d47',
        '0x2300c0255fbe8cee1392db4c93d6059ca88a7453ee1bb1a67ef1b1ccfa11932b'
    )

    message_text = "I♥SF"
    msghash = encode_defunct(text=message_text)
    signature = Account.sign_message(msghash, acc.key)
    # code.interact(local=locals())

    recoveredMsg = Account.recover_message(msghash, signature=signature.signature)
    print('account:\n . address:', acc.address, '\n . pubkey', acc.public_key, '\n . privkey:', to_hex(acc.key))
    print('\n')
    print('recovered message', recoveredMsg)

def web3_account_update_multisig():
    user1_updator = Account.from_key('0x8b0164c3a59d2b1a00a9934f85ae77c14e21094132c34cc3daacd9e632c90807')
    user2 = Account.create()
    user3 = Account.create()

    valueTransferTx = transaction.empty_tx(transaction.TX_TYPE_VALUE_TRANSFER)
    valueTransferTx['from'] = user1_updator.address
    valueTransferTx['to'] = '0x6574b98b232bdD2C94Bf07CadE3651eD309E38e0'
    valueTransferTx['value'] = 3000000000000
    valueTransferTx['chainId'] = 2019
    valueTransferTx['nonce'] = 10
    transaction.fill_transaction(valueTransferTx)
    signedTx = Account.sign_transaction(valueTransferTx, user1_updator.key)
    result = w3.eth.send_raw_transaction(signedTx.rawTransaction)
    print(result.hex())

web3_account_update_multisig()