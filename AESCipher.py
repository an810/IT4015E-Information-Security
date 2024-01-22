import base64
import hashlib
from aes import run, Direction

class AESCipher(object):

    def __init__(self, key, cipher_file_path):
        self.bs = 16
        self.key = key
        self.cipher_file_path = cipher_file_path

    def encrypt(self, raw):
        # use the run function from aes.py for encryption
        encrypted_data = run(Direction.ENCRYPT, raw, self.key, self.cipher_file_path)
        return encrypted_data

    def decrypt(self, enc):
        # use the run function from aes.py for decryption
        decrypted_data = run(Direction.DECRYPT, enc, self.key, self.cipher_file_path)
        return decrypted_data

