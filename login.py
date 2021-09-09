from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
import time
from keyboard import press
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("nwapp=C:/Users/Me/Documents/POS_Application/2021-09-09/backup/frontend/KRAKEN_RESTO.exe")

driver = webdriver.Chrome("C:/Users/Me/Documents/POS_Application/2021-09-09/backup/nwjs-sdk-v0.54.0-win-x64/chromedriver.exe", options= options)


#maximize window
driver.maximize_window()
time.sleep(2)