# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:50:27 2021

@author: LENOVO
"""

import pyAesCrypt
import os
from time import sleep as sl

buffersize = 64 * 1024

password = input("Enter your password : ")

Except = input("Enter E for encryption , Enter D for decryption .")

filename = input("Enter the name of your file :")

str(filename)

if Except == "E":
    
    try:
        pyAesCrypt.encryptFile(filename , "logs.txt.aes" , password , buffersize)
        sl(1)
        os.remove(filename)
        print("succes")
        
    except EOFError as err :
        print(err)
        
elif Except == "D":
    try:
        pyAesCrypt.decryptFile(filename , "logs.txt" , password , buffersize)
        sl(1)
        os.remove('logs.txt.aes')
        print("Decrypt succes")
        
    except EOFError as er :
        print(er)

else:
    print("Wrong input given")
    