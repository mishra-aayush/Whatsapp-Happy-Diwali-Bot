# Whatsapp Bot

Replying the same thing to each and every Whatsapp contact on Diwali can get frustrating, therefore this bot was created to reply to all the Happy Diwali wishes on your Whatsapp. This year, have a hassle free Diwali.

## Steps for use

1. Ensure that the appropriate webdriver is installed and the appropriate steps are followed. Use this as a reference - [Webdrivers documentation](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/)

2. Execute the pyton file on your terminal

3. Scan the Whatsapp QR code using your mobile device

## Important Note
   
1. The class names may vary from system to system, therefore if the code does not work, the code may not be able to access the given class names. In that case, the user must manually change the class names of required elements after inspecting the [Web Whatsapp](https://web.whatsapp.com/) page.

2. The process is entirely automated, except the QR scanning for opening Whatsapp, for security reasons, the user has to manually scan the QR code with their phone.

3. This code is written using the [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), but webdrivers for other browsers can be downloaded from here: 
    - [Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 
    - [Geckodriver for Mozilla](https://github.com/mozilla/geckodriver/releases) 
    - [Safari Webdriver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) 
    
    Make sure that the webdriver is in installed and executed in the same location as this python script.
    Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException`
    
