#made by Armandukx
#imports
import os
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
print("")
#MADE BY ARMANDUKX
#imports continue
import colorama
from colorama import Fore
import time
import pyfiglet
from pyfiglet import figlet_format
from tkinter import *
import os
import pyperclip
import time
#start
print(Fore.LIGHTGREEN_EX + '') #Color for the text
print(figlet_format("Armandukx", font = "speed"))
print(Colorate.Horizontal(Colors.blue_to_red, f"Join our discord to be up to date! https://discord.gg/qrRZvdT73s"))
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
    driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    driver.get("https://zefoy.com/")
    url='https://zefoy.com/'
    time.sleep(10)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/div/div/div/button")
    driver.set_window_position(-10000,0)#1 SHARES
    print(Colorate.Horizontal(Colors.red_to_purple, f"Sending Shares..."))
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(4)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(4)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(4)
    s1 = (videourl) #copy's the video url
    pyperclip.copy(s1)
    s2 = pyperclip.paste()
    print(s2) #end of copying and pasting.
    keyboard.press_and_release('ctrl+v')
    time.sleep(4)
    #MADE BY ARMANDUKX
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    time.sleep(4)
    element = driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div[1]/div/form/button")
    driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
    element.click()
    print(Colorate.Horizontal(Colors.red_to_purple, f"Ignore that ^ its just google stuff..."))
    time.sleep(10)
    driver.quit()
    print(Colorate.Horizontal(Colors.red_to_purple, f"Sent Shares..."))
    print(Colorate.Horizontal(Colors.red_to_purple, f"You must wait 5-8 minute's before trying again!"))
    time.sleep(20)
    quit()
else: driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
driver.get("https://zefoy.com/")
url='https://zefoy.com/'
time.sleep(10)
element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/div/div/div/button")
driver.set_window_position(-10000,0)#1 SHARES
print(Colorate.Horizontal(Colors.red_to_purple, f"Sending Views..."))
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(4)
element = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(4)
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/input")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(4)
s1 = (videourl) #copy's the video url
pyperclip.copy(s1)
s2 = pyperclip.paste()
print(s2) #end of copying and pasting.
keyboard.press_and_release('ctrl+v')
time.sleep(4)
#MADE BY ARMANDUKX
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/div/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
time.sleep(4)
element = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/div[1]/div/form/button")
driver.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
print(Colorate.Horizontal(Colors.red_to_purple, f"Ignore that ^ its just google stuff..."))
time.sleep(10)
driver.quit()
print(Colorate.Horizontal(Colors.red_to_purple, f"Sent Views"))
print(Colorate.Horizontal(Colors.red_to_purple, f"You must wait 5-8 minute's before trying again!"))
time.sleep(20)
quit()
