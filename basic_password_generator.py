


import random
import logging

space ="  "

chars= "abcdefghikklmnopqrstuvwxyzABCDEFGHOJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?<>"




logging.basicConfig(filename ="logs.txt",
                    filemode="a",
                    format= '%(asctime)s %(levelname)-s%(message)s',
                    datefmt='%y-%m-%d %H:%M:%S')
                    
                 
work="yes"




while work == "Yes" or work == "yes" :
    
    
    password_len = int(input("What is the length of your password :"))
    
    subject= input("For what are you generating password : ")
    password = ""
    
        
    for x in range (0,password_len):
        password_char = random.choice(chars)
        password = password + password_char
    
    
   
    
    print("Here is your password for your" , subject , "account " , password )
    logging.warning(" Here is your password for your " + subject + " account" + str(space) +  str(password))
    
    work = input("Do you want to continue : ")

 
