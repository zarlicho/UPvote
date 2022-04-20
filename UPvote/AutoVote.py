from re import sub
from xmlrpc.client import boolean
from selenium import webdriver
from sympy import false
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import subprocess
import requests
driver = webdriver.Chrome(ChromeDriverManager().install())
url2 = ('https://www.croxyproxy.com/')
vote = ("//*[@id='__next']/div[1]/div/div/main/section[1]/div[2]/span/button")
clos = ("/html/body/div/div[1]/div/div/main/div[3]/button")
GOBTN = "//*[@id='requestSubmit']"
EnterURL = "https://coinmooner.com/coin/17487"
EnterURLSelector = "//*[@id='url']" 

actions = ActionChains(driver)
time.sleep(3)
# driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/main/section[1]/div[2]/span/button").click()
x = False
def GetVote():
    while True:
        try:
            x = False
            if x == False:
                driver.get(EnterURL)
            # InputURL = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, EnterURLSelector)))
            # InputURL.send_keys(EnterURL)
            # time.sleep(2)
            # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, GOBTN))).click() 
            # time.sleep(2)
            # el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, vote)))
            # ActionChains(driver).move_to_element(el).perform()
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, clos))).click() 
            el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, vote)))
            ActionChains(driver).move_to_element(el).perform()
            # /html/body/div/div[1]/div/div/main/section[1]/div[2]/span/button
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, vote))).click() 
            driver.delete_all_cookies()
            time.sleep(1)
            subprocess.call('netsh interface set interface name="Ethernet" admin=DISABLED', shell=True)
            time.sleep(1)
            subprocess.call('netsh interface set interface name="Ethernet" admin=ENABLED', shell=True)
        except:
            x = True
            print("Disconnected")


