import json
import copy
from web3 import Web3

# Account key type in klaytn
ACCOUNT_KEY_NIL_TAG = '0x80'
ACCOUNT_KEY_LEGACY_TAG = '0x01'
ACCOUNT_KEY_PUBLIC_TAG = '0x02'
ACCOUNT_KEY_FAIL_TAG = '0x03'
ACCOUNT_KEY_WEIGHTED_MULTISIG_TAG = '0x04'
ACCOUNT_KEY_ROLE_BASED_TAG = '0x05'

# Reserve role type in role based key
ROLE_TRANSACTION_KEY = 0
ROLE_ACCOUNT_UPDATE_KEY = 1
ROLE_FEE_PAYER_KEY = 2
ROLE_LAST = 3

# Maximum key number in multisig/rolebased
MAXIMUM_KEY_NUM = 10

class AcstractAccountStore:
    def __init__(self):
        self.account_store = {}

    def add(self, address, keyring):
        if not Web3.is_address(address):
            return False
        if self.validate_keyring(keyring):
            return False
         
        self.account_store[address] = keyring
        return True
    
    def is_in_account_store(self, address):
        if address in self.account_store.keys():
            return True
        return False

    def delete(self, address):
        if self.is_in_account_store(address):
            self.account_store.pop(address)

    def get_account(self, address):
        if self.is_in_account_store(address):
            account = copy.deepcopy(self.account_store[address])
            account['address'] = address
            return account
    
    # Generate empty keyring case
    # You can use it for AccountUpdateTransaction after adding/appending keys according to the key types
    def empty_keyring(self, keyring_type):
        if keyring_type == ACCOUNT_KEY_NIL_TAG:
            return {}
        elif keyring_type == ACCOUNT_KEY_FAIL_TAG:
            return {'type' : ACCOUNT_KEY_FAIL_TAG}
        elif keyring_type == ACCOUNT_KEY_LEGACY_TAG:
            return {'type' : ACCOUNT_KEY_LEGACY_TAG}
        elif keyring_type == ACCOUNT_KEY_PUBLIC_TAG:
            return {
                'type' : ACCOUNT_KEY_PUBLIC_TAG,
                'key' : {}
            }
        elif keyring_type == ACCOUNT_KEY_WEIGHTED_MULTISIG_TAG:
            return {
                'type': ACCOUNT_KEY_WEIGHTED_MULTISIG_TAG,
                'threshold':0,
                'keys' : {}
            }
        elif keyring_type == ACCOUNT_KEY_ROLE_BASED_TAG:
            return {
                'type' : ACCOUNT_KEY_ROLE_BASED_TAG,
                'keys' : {
                    'roleTransactionKey' : {},
                    'rolwAccountUpdateKey' : {},
                    'roleFeePayerKey' : {}
                }
            }

    def validate_keyring(self, keyring):
        pass

    def key_info(self, key):
        pass