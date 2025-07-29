import base64
import os
import json
from crypto import encrypt_data, decrypt_data 

VAULTFILE = "vault.json"

def create_vault(master_password):
    salt = os.urandom(16)
    vault_data = {}
    vault_contents = encrypt_data(vault_data, master_password, salt) 
    with open(VAULTFILE, 'w') as f:
        json.dump(vault_contents, f)
    print("New Vault created")
    return vault_data, salt


def load_vault(master_password):
    with open(VAULTFILE, 'r') as f:
        vault_contents = json.load(f)
    salt = base64.b64decode(vault_contents['salt'])
    data = decrypt_data(vault_contents, master_password)
    return data, salt


def save_vault(vault_data, master_password, salt):
    encrypted_vault = encrypt_data(vault_data, master_password, salt)
    with open(VAULTFILE, 'w') as f:
        json.dump(encrypted_vault, f)
    print("Vault saved")

