import time
import random
import string
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("nwapp=C:/Users/Me/Documents/POS_Application/2021-09-09/backup/frontend/KRAKEN_RESTO.exe")
driver = webdriver.Chrome("C:/Users/Me/Documents/POS_Application/2021-09-09/backup/nwjs-sdk-v0.54.0-win-x64/chromedriver.exe", options= options)

def functionLog():
 #MAX WIN
 driver.maximize_window()
 time.sleep(2)


 item = pd.read_excel("itemClass_subclass.xls","itemClass")

# Saving Excel File Columns as List / Array
 Item_class = item["Item_class"].values.tolist()
 


 #lOGIN

 port = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input")
 port.send_keys(Keys.BACKSPACE)
 port.send_keys(4)

 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[7]/ion-col/button[2]").click()
 time.sleep(6)

 alert = driver.switch_to.alert
 time.sleep(2)
 alert.accept() 
 time.sleep(15)

 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[5]/ion-col[2]/input").send_keys("OMK-ZHN-AOC-WPO-NNN-AAE-MOR-WMO-APY-NPR")
 time.sleep(2)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[6]/ion-col/button/span").click()
 time.sleep(2)

 #user id
 driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys("lstv")
 time.sleep(2)

 #user password
 driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys("lstventures")
 time.sleep(2)

 driver.execute_script("document.querySelectorAll('.button-default-md.button-block.button-block-md')[0].click();")

 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.menubutton')[5].click();")
 time.sleep(4)
 #terminal
 driver.find_element_by_xpath("//*[@id='lbl-5']").click()
 time.sleep(6)
 driver.execute_script("document.querySelectorAll('.fab.fab-md')[1].click();")
 time.sleep(4)
 def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

 chars = string.digits
 size = 4
 terminal = ('TERMINAL ', random_string_generator(size, chars))
 station = ('STATION ', random_string_generator(size, chars))
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(terminal)
 time.sleep(2)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-terminal-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[2]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys("127.0.0.1")
 time.sleep(2)
 

 driver.execute_script("document.querySelectorAll('.center.button.button-md.button-outline.button-outline-md')[0].click();")
 time.sleep(8)
 back = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-terminal/ion-header/ion-navbar/ion-buttons/button")
 back.click()
 time.sleep(4)
 #Printer Station
 driver.execute_script("document.querySelectorAll('.label.label-md')[4].click();")
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.fab.fab-md')[1].click();")
 time.sleep(2)
    #station name
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(station)
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[0].click();") #terminal
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[3].click();") #terminal rdb 
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[1].click();") #printer name
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[5].click();")#printer name rdb 
 time.sleep(6)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[2].click();")#printer type
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.item-cover-default-md')[3].click();") #printer type rdb 
 time.sleep(4)
 driver.execute_script("document.querySelectorAll('.text-input.text-input-md')[1].click();") #printer size
 time.sleep(2)
 ps = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-locations-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[4]/ion-col[2]/ion-item/div[1]/div/ion-input/input")
 ps.click()
 time.sleep(2)
 ps.send_keys("4") #printer pp size
 time.sleep(2)
 driver.execute_script("document.querySelectorAll('.button-outline-md')[2].click();") 
 time.sleep(2)
 driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-locations/ion-header/ion-navbar/ion-buttons").click()
 time.sleep(2)
 driver.execute_script("document.querySelectorAll('.label.label-md')[7].click();")
 time.sleep(4)
 
 
 for f in range(len(Item_class)):
  time.sleep(8)
  driver.execute_script("document.querySelectorAll('.fab.fab-md')[1].click();")
  time.sleep(8)
  #Item Class 

  time.sleep(4)
  item = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-item-class-crud/ion-content/div[2]/form/ion-card/ion-grid/ion-row[1]/ion-col/ion-item/div[1]/div/ion-input/input")
  item.click()
  time.sleep(4)
  item.send_keys(Item_class[f])
  time.sleep(2)
  driver.execute_script("document.querySelectorAll('.item-cover-default-md')[0].click();")
  time.sleep(2)
  driver.execute_script("document.querySelectorAll('.alert-checkbox-button-default-md')[1].click();")
  time.sleep(2)
  #ok btn
  driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").click()
  time.sleep(2)
  
 #add btn
 driver.execute_script("document.querySelectorAll('.center.button.button-md.button-outline.button-outline-md')[1].click();")
 time.sleep(2)
functionLog()  


