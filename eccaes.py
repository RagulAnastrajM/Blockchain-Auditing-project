import pyAesCrypt
import os
from cryptography.fernet import Fernet
import hashlib


from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64, os


secp_k = generate_key()
privhex = secp_k.to_hex()
pubhex = secp_k.public_key.format(True).hex()

print(pubhex)

def encrypt(key,source,des):
    output=des
    pyAesCrypt.encryptFile(source,output,key)
    return output

def decrypt(key,source,des):
    dfile=source.split(".")
    output=des

    pyAesCrypt.decryptFile(source,output,key)
    return output


password = pubhex

print(password)
#password = randStr(chars='abcdef123456')
#key = str(password)
key = password
print(key)

tail ="450adminLogin.jpg"
newfilepath1 = './static/upload/' + str(tail)
newfilepath2 = './static/Encrypt/' + str(tail)
newfilepath3 = './static/Decrypt/' + str(tail)
encrypt(key,newfilepath1,newfilepath2)

decrypt(key,newfilepath2,newfilepath3)



#souce ="123.jpg.enc"
#fen=encrypt(key,souce)
#decrypt(key,souce)