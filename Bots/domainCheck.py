from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print("Initiating the bot...\n")

'''deprecated mode
PATH = 'C:/Users/Pc/Desktop/Luiz/Robos/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://registro.br/")
'''

#cleaner mode
ser = Service('C:/Users/Pc/Desktop/Luiz/Robos/chromedriver')
op = webdriver.ChromeOptions()
#option to remove bluetooth adapter error
op.add_experimental_option("excludeSwitches", ["enable-logging"]) 

driver = webdriver.Chrome(service=ser, options=op)

url = "https://registro.br/"
driver.get(url)

search = driver.find_element(By.ID,"is-avail-field")
search.clear() #Cleaning the search bar
domain = "roboscompython.com.br"
search.send_keys(domain)

search.send_keys(Keys.RETURN)
time.sleep(2) #time to load the page

#find information with a Tag
results = driver.find_elements(By.TAG_NAME,"strong")

#import pdb; pdb.set_trace() 
#method to stop the code and trace the results by results[i].text. (c + enter closes it)

#print results
print("Domain %s %s" % (domain, results[4].text))

time.sleep(4) #Time for conclusion
driver.close()