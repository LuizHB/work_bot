from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print("Initiating the bot...\n")

#webdriver - chromedriver version 100.0.4896.127
ser = Service()
op = webdriver.ChromeOptions()
#option to remove bluetooth adapter error
op.add_experimental_option("excludeSwitches", ["enable-logging"]) 
driver = webdriver.Chrome(service=ser, options=op)
url = "https://registro.br/"
driver.get(url)





driver.close()