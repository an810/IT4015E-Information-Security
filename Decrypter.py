import base64
import hashlib
from AESCipher import AESCipher
from PIL import Image
from random import randint
class Decrypter:
    def __init__(self, cipher, cipher_file_path):
        self.cipher = cipher
        self.cipher_file_path = cipher_file_path
    def decrypt_image(self,k):
        key = k
        cipher = self.cipher
        aes = AESCipher(key, self.cipher_file_path)
        base64_decoded = aes.decrypt(cipher)
        # fh = open(f"decryptedImage{self.cipher_file_path}.png", "wb")
        fh = open(f"decryptedImage{self.cipher_file_path}", "wb")
        fh.write(base64.b64decode(base64_decoded))
        fh.close() 
        return (base64.b64decode(base64_decoded))
        