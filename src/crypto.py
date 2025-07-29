import base64
import json
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password, salt):
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


def encrypt_data(data_dict, password, salt):
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    data_json = json.dumps(data_dict)
    encrypted = aesgcm.encrypt(nonce, data_json.encode(), None)
    return {
        "salt": base64.b64encode(salt).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "data": base64.b64encode(encrypted).decode()
    }


def decrypt_data(vault_contents, master_password):
    salt = base64.b64decode(vault_contents['salt'])
    nonce = base64.b64decode(vault_contents['nonce'])
    encrypted = base64.b64decode(vault_contents['data'])
    key = derive_key(master_password, salt)
    aesgcm = AESGCM(key)
    decrypted = aesgcm.decrypt(nonce, encrypted, None)
    return json.loads(decrypted.decode())

