import base64
import hashlib
from AESCipher import AESCipher
from PIL import Image
from random import randint
class Encrypter:
    def __init__(self, text,key, cipher_file_path):
        self.text = text
        self.key =  key
        self.cipher_file_path = cipher_file_path
    def encrypt_image(self):
        aes = AESCipher(self.key, self.cipher_file_path)
        print(self.text)
        cipher = aes.encrypt(self.text)

        return cipher
