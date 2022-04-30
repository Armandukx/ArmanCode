#made by Armandukx
#imports
from ssl import Options
import pystyle
from pystyle import Colorate, Colors, Write
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
import numpy as np
import keyboard #imports the keyboard
print('getting "chromedriver.exe" location')
print("")
import os
 
# This is to get the directory that the program
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__))
 
for root, dirs, files in os.walk(dir_path):
    for file in files:
 
        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith('.exe'):
            f = open("TEMP.txt","w+")
            f.write(root+'/'+str(file))
            f.close()
            f = open('TEMP.txt', 'r')
            contents = f.read()
            print(contents)
            f.close()
print("")
print ("")
print("license")
print("")
#LICENSE
print("--Terms & Conditions--")
print("By using our app you agreed with our terms and conditions.")
print("--Notice--")
print("We are not responsible for any damage/claims in any case, use at your own risk.")
print("--Rights--")
print("We have all the rights to change/modify our terms & conditions/privacy policy at any time.")
print("If you don't agree with our terms & conditions, you should stop using our services..")
print("")
print(Colorate.Horizontal(Colors.purple_to_blue, f"Designer and Coder: Armandukx"))
#MADE BY ARMANDUKX
#imports continue
import colorama
from colorama import Fore
import time
from tkinter import *
import os
import pyperclip
import time
#start
print(Colorate.Horizontal(Colors.green_to_red, f"_______                                _________      ______         "))
print(Colorate.Horizontal(Colors.green_to_red, f"___    |_____________ _________ _____________  /___  ____  /_____  __"))
print(Colorate.Horizontal(Colors.green_to_red, f"__  /| |_  ___/_  __ `__ \  __ `/_  __ \  __  /_  / / /_  //_/_  |/_/"))
print(Colorate.Horizontal(Colors.green_to_red, f"_  ___ |  /   _  / / / / / /_/ /_  / / / /_/ / / /_/ /_  ,<  __>  <  "))
print(Colorate.Horizontal(Colors.green_to_red, f"/_/  |_/_/    /_/ /_/ /_/\__,_/ /_/ /_/\__,_/  \__,_/ /_/|_| /_/|_|  ")) # https://patorjk.com/software/taag/#p=display&f=Speed&t=Armandukx
print("")
print(Colorate.Horizontal(Colors.blue_to_red, f"Join our discord to be up to date! https://discord.gg/qrRZvdT73s"))
print("")
print(Colorate.Horizontal(Colors.red_to_purple, f"IMPORTANT: if you get some google error that means you're on a timer"))
print("")
print(Colorate.Horizontal(Colors.red_to_purple, f"[0] - Views ? > "))
print(Colorate.Horizontal(Colors.red_to_purple, f"[1] - Share ? > "))
Chosen = Write.Input("", Colors.red_to_purple, interval=0.0001)
videourl = Write.Input("Url of the video ? > ", Colors.red_to_purple, interval=0.0001)
s1 = (videourl) #copy's the video url
pyperclip.copy(s1)
s2 = pyperclip.paste()
print(s2) #end of copying and pasting.
if Chosen.lower().startswith("1"):
    driver = webdriver.Chrome(contents)
    driver.get("https://zefoy.com/")
    url='https://zefoy.com/'
    time.sleep(10)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/div/div/div/button")
    driver.set_window_position(-10000,0)#1 SHARES
    print(Colorate.Horizontal(Colors.red_to_purple, f"Sending Shares..."))
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(2)
    s1 = (videourl) #copy's the video url
    pyperclip.copy(s1)
    s2 = pyperclip.paste()
    print(s2) #end of copying and pasting.
    keyboard.press_and_release('ctrl+v')
    time.sleep(2)
    #MADE BY ARMANDUKX
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(4)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div[1]/div/form/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    print(Colorate.Horizontal(Colors.red_to_purple, f"Ignore that ^ its just google stuff..."))
    print("")
    print(Colorate.Horizontal(Colors.red_to_purple, f"Finishing stuff up.."))
    print("")
    time.sleep(10)
    driver.quit()
    print(Colorate.Horizontal(Colors.red_to_purple, f"Sent Shares Successfully!"))
    print("")
    print(Colorate.Horizontal(Colors.red_to_purple, f"You must wait 5-8 minute's before trying again!"))
    if os.path.exists("TEMP.txt"):
          os.remove("TEMP.txt") #delets the .txt file
    time.sleep(20)
    quit()
else: driver = webdriver.Chrome(contents)
driver.get("https://zefoy.com/")
url='https://zefoy.com/'
time.sleep(10)
element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/div/div/div/button")
driver.set_window_position(-10000,0)#1 SHARES
print(Colorate.Horizontal(Colors.red_to_purple, f"Sending Views..."))
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/input")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(2)
s1 = (videourl) #copy's the video url
pyperclip.copy(s1)
s2 = pyperclip.paste()
print(s2) #end of copying and pasting.
keyboard.press_and_release('ctrl+v')
time.sleep(2)
#MADE BY ARMANDUKX
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/div/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(4)
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/div[1]/div/form/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
print(Colorate.Horizontal(Colors.red_to_purple, f"Ignore that ^ its just google stuff..."))
print("")
print(Colorate.Horizontal(Colors.red_to_purple, f"Finishing stuff up.."))
print("")
time.sleep(10)
driver.quit()
print(Colorate.Horizontal(Colors.red_to_purple, f"Sent Views Successfully!"))
print("")
print(Colorate.Horizontal(Colors.red_to_purple, f"You must wait 5-8 minute's before trying again!"))
if os.path.exists("TEMP.txt"):
          os.remove("TEMP.txt") #delets the .txt file
time.sleep(20)
quit()
