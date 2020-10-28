# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:08:57 2020

A bot that automatically replies to all the Happy Diwali wishes on Whatsapp. 

@author: AAYUSH MISHRA
"""

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='E:\chromedriver')
browser.get('https://web.whatsapp.com/')

msg = "Thank you and a very Happy Diwali to you too!"

input('Enter any key after scanning QR code')
time.sleep(7)

titles = browser.find_elements_by_class_name("_3CneP")

names_list = []
for info in titles:
    names_list.append(info.text)

for name in names_list:
    try:
        person = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        person.click()
        
        for i in range(1,5):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        message_list = browser.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        messages = []
        for message in message_list:
            messages.append(message.text)
            
        if "happy" in messages[-1].lower() and "diwali" in messages[-1].lower():
            message_box = browser.find_element_by_xpath('//div[@class="_3uMse"]')
            message_box.send_keys(msg)

            message_button = browser.find_element_by_xpath('//button[@class="_1U1xa"]')
            message_button.click()

    except:
        #Exceptions can occour if emojis present in names
        continue

browser.close()