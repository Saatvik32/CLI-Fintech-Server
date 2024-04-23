from sha import sha256
from datetime import datetime
import os
import re
import pandas as pd
from termcolor import colored
import time
import pyotp
import pyqrcode
from PIL import Image
from lsfr import generateID
from secret import generateSecret
from aes import encrypt as aes_encryption ,decrypt as aes_decryption
import base64


USER_PATH = 'database2/user.txt'
HISTORY_PATH = 'database2/history.txt'

def encryptDatabase(secret):

    with open(os.path.join(os.path.dirname(__file__), USER_PATH), 'r') as f:
            data = f.read()

    cipher = aes_encryption(str.encode(secret),str.encode(data))
    cipher = base64.b64encode(cipher)
    cipher = cipher.decode("utf-8")
    user_obj = open('database2/user.txt','w')
    user_obj.write(cipher)

    with open(os.path.join(os.path.dirname(__file__), HISTORY_PATH), 'r') as f:
            data = f.read()

    cipher = aes_encryption(str.encode(secret),str.encode(data))
    cipher = base64.b64encode(cipher)
    cipher = cipher.decode("utf-8")
    history_obj = open('database2/history.txt','w')
    history_obj.write(cipher)


def create_new_secret_key():
    new_key = str(generateSecret()) + str(generateSecret())
    new_key = new_key[:16]
    sk_obj = open('secret_key.txt','w')
    sk_obj.write(new_key)
    return new_key


new_key = create_new_secret_key()
encryptDatabase(secret=new_key)

