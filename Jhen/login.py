import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("nwapp=C:/Users/Me/Documents/POS_Application/2021-09-09/backup/frontend/KRAKEN_RESTO.exe")
driver = webdriver.Chrome("C:/Users/Me/Documents/POS_Application/2021-09-09/backup/nwjs-sdk-v0.54.0-win-x64/chromedriver.exe", options= options)

#MAX WIN
driver.maximize_window()
time.sleep(2)

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
