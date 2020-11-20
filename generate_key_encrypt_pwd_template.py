# -*- coding: utf-8 -*-

import cx_Oracle
import pandas as pd
import numpy as np
import os
os.chdir('<target directory>')
os.getcwd()

#Generate CryptoKey and save to a file.
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('.\Key.bin', 'wb') as file_object:  file_object.write(key)
print(key)

#encrypt password
with open('.\Key.bin', 'rb') as keyfile_object:
    for line in keyfile_object:
        key = line

cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b'<password>')
with open('.\pwd_bytes.bin', 'wb') as file_object:  file_object.write(ciphered_text)


#test connection with encrypted password
with open('.\Key.bin', 'rb') as keyfile_object:
    for line in keyfile_object:
        key = line

cipher_suite = Fernet(key)
with open('.\pwd_bytes.bin', 'rb') as pwdfile_object:
    for line in pwdfile_object:
        pwdadwc = line
uncipher_text = (cipher_suite.decrypt(pwdadwc))
text_pwdadwc = bytes(uncipher_text).decode("utf-8") #convert to string


adwc = cx_Oracle.connect("Jason_Hosler", text_pwdadwc, "adwce19c_medium")
table_list = pd.read_sql("select OWNER, TABLE_NAME from all_tables where OWNER = 'ADWCPROD_OWNER'", con=adwc)
adwc.close()


