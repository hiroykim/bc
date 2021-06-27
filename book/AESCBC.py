import sys
#import crypto
#sys.modules['Crypto'] = crypto
import numpy as np
from Crypto import Random
from Crypto.Cipher import AES


secretKey128 = b'0123456701234567'
secretKey192 = b'012345670123456701234567'
secretKey256 = b'01234567012345670123456701234567'

secretKey = secretKey128
plainText = "This is Plain text, It will be encrypted using AES with CBC mode."
print("\n\n")
print("원문 : ")
print(plainText)

n = len(plainText)
if (n % 16) != 0:
    n = n + 16 - (n % 16)
    plainText = plainText.ljust(n, '\0')

print("패딩적용 : ")
print(plainText)

iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv)
print("iv, ivcopy : ")
print(iv, ivcopy)