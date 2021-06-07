import pyAesCrypt
import os
from time import sleep as sl

buffersize = 64 * 1024

mk = input("Enter your master password : ")

password = "abc@1234" #keep the password for the encryption of the file



if mk == "abc@1234": #keep your master password
    
    
    Except = input("Enter E for encryption , Enter D for decryption .")

    filename = input("Enter the name of your file :")

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
            pyAesCrypt.decryptFile(filename , "logs.jpeg" , password , buffersize)
            sl(1)
            os.remove('logs.txt.aes')
            print("Decrypt succes")
        
        except EOFError as er :
            print(er)

    else:
        print("Wrong input given")
        
else:
    print("Wrong password")
    
