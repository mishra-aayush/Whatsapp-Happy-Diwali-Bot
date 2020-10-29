# Whatsapp Bot

Replying the same thing to each and every Whatsapp contact on Diwali can get get frsutrating, therefore this bot was created to reply to all the Happy Diwali wishes on your Whatsapp. This year, have a hassle free Diwali.

## Steps for use

1. Ensure that the appropriate webdriver is installed and the appropriate steps are followed. Use this as a reference - [Webdrivers documentation](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/)

2. Execute the pyton file on your terminal

3. Scan the Whatsapp QR code using your mobile device

## Note

1. If you have pip on your system, you can simply install or upgrade the Python bindings:
    
    `pip install -U selenium`
    
    Alternately, you can download the source distribution from [PyPI](https://pypi.org/project/selenium/#files), unarchive it, and run:
    
    `python setup.py install`
   
2. The class names may vary from system to system, therefore if the code does not work, just manually change the class name after inpecting the [Web Whatsapp](https://web.whatsapp.com/) page.

3. The process is entirely automated, except the QR scanning for opening Whatsapp, for security reasons, the user has to manually scan the QR code with their phone.

4. This code is written using the [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), but webdrivers for other browsers can be downloaded from here: 
    - [Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 
    - [Geckodriver for Mozilla](https://github.com/mozilla/geckodriver/releases) 
    - [Safari Webdriver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) 
    
    Make sure that the webdriver is in installed and executed in the same location as this python script.
    Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException`
    
