# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:08:57 2020

A bot that automatically replies to all the Happy Diwali wishes on Whatsapp. 

@author: AAYUSH MISHRA
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#Eliminates the need to install webdrivers manually
browser = webdriver.Chrome(ChromeDriverManager().install())

#Launching the browser and opening the webpage
browser.get('https://web.whatsapp.com/')

#Custom message
print("What is your reply?")
msg = input("Enter here: ")

#Preventing the error of trying to access elements before they appear on the page
input('Enter any key after scanning QR code')
time.sleep(7)

#Find the list of all names in the chat section
titles = browser.find_elements_by_class_name("_3CneP")
names_list = []
for info in titles:
    names_list.append(info.text)

for name in names_list:
    try:
        #Open the chat of a specific person
        person = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        person.click()
        
        for i in range(1,5):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        #Get the list of messages exchanged with the person
        message_list = browser.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        messages = []
        for message in message_list:
            messages.append(message.text)
            
        #Checking the last message
        if "happy" in messages[-1].lower() and "diwali" in messages[-1].lower():
            #Navigate to the type message here section
            message_box = browser.find_element_by_xpath('//div[@class="_3uMse"]')
            #Typing message in that section
            message_box.send_keys(msg)
            #Accessing the send button
            message_button = browser.find_element_by_xpath('//button[@class="_1U1xa"]')
            #Clicking the send button
            message_button.click()

    except:
        #Exceptions can occour if emojis present in names
        continue
#Close the browser
browser.close()
