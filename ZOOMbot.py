# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:55:31 2021

@author: LENOVO
"""
#-----------------------------------------------------------------
#-----------------------------------------------------------------

import datetime
from selenium import webdriver
import keyboard
import time
import schedule

#-----------------------------------------------------------------
#-----------------------------------------------------------------

Class_1 = ("04:05:00")
Class_2 = ("06:35:00")

#-----------------------------------------------------------------
#-----------------------------------------------------------------

#-----------------------------------------------------------------

Class1_link = ("https://tutoratti.zoom.us/j/83402840947?pwd=MXo4L2lQc0pNRGxFSGloMWZTOXdidz09")

Class2_link =("https://tutoratti.zoom.us/j/89601635244?pwd=cHlXRXQvY2x0T2U0U1A1QWs1amordz09")

#-----------------------------------------------------------------
#-----------------------------------------------------------------

date_logs = datetime.datetime.now()

#-----------------------------------------------------------------

current_day =(date_logs.strftime("%a"))
print(current_day)

#-----------------------------------------------------------------

current_time =date_logs.strftime("%H:%M:%S")
print(current_time)

#-----------------------------------------------------------------

def zoomJoin():
    time.sleep(2)
    keyboard.press_and_release('tab' , do_press=(True) , do_release=(True))
    time.sleep(3)
    keyboard.press_and_release('tab' , do_press=(True) , do_release=(True))
    time.sleep(3)
    keyboard.press_and_release('enter' , do_press=(True) , do_release=(True))

def joinClass1 ():
    driver=webdriver.Chrome()
    driver.get(Class1_link)
    time.sleep(10)
    
    #_joins_the_class.
    zoomJoin()
    time.sleep(7200)
    driver.quit()   
    
def joinClass2 ():
    driver=webdriver.Chrome()
    driver.get(Class2_link)
    time.sleep(10)
    
    #_joins_the_class.
    zoomJoin()
    time.sleep(7200)
    driver.quit()





#----------------------------------------------------------------------------------
#monday
schedule.every().monday.at(Class_1).do(joinClass1)
schedule.every().monday.at(Class_2).do(joinClass2)

#tuesday
schedule.every().tuesday.at(Class_1).do(joinClass1)
schedule.every().tuesday.at(Class_2).do(joinClass2)

#Wednesday
schedule.every().wednesday.at(Class_1).do(joinClass1)
schedule.every().wednesday.at(Class_2).do(joinClass2)

#thursday
schedule.every().thursday.at(Class_1).do(joinClass1)
schedule.every().thursday.at(Class_2).do(joinClass2)

#friday
schedule.every().friday.at(Class_1).do(joinClass1)
schedule.every().friday.at(Class_2).do(joinClass2)
#----------------------------------------------------------------------------------


while True :
    schedule.run_pending()
    time.sleep(1)
    
    


    
    
    
    
    
    
    
    
    