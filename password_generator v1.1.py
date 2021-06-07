from cryptography.fernet import Fernet
import random
import logging

space ="  "

chars= "abcdefghikklmnopqrstuvwxyzABCDEFGHOJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?<>"

key = "iGY94lnyM9iEdWIadNmWlWU-EzeF0iMlEr4xDvAhKc4="

master_key = input("Enter the master key to start the program : ")

crypter = Fernet(key)

logging.basicConfig(filename ="logs.txt",
                    filemode="a",
                    format= '%(asctime)s %(levelname)-s%(message)s',
                    datefmt='%y-%m-%d %H:%M:%S')
                    
                 
work="yes"


if master_key=="abc@123":

    while work == "Yes" or work == "yes" :
    
    
        password_len = int(input("What is the length of your password :"))
    
        subject= input("For what are you generating password : ")
        password = ""
    
        
        for x in range (0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
    
    
        new1= bytes(password , "ascii")
        new=  crypter.encrypt(new1)
    
        print("Here is your password for your" , subject , "account " , new )
        print(password)
        logging.warning(" Here is your password for your " + subject + " account" + str(space) +  str(new))
    
        work = input("Do you want to continue : ")

else:
    print("Bad Auth")       
