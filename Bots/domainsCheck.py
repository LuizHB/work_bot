from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print("Initiating the bot...\n")

#webdriver
ser = Service()
op = webdriver.ChromeOptions()
#option to remove bluetooth adapter error
op.add_experimental_option("excludeSwitches", ["enable-logging"]) 
driver = webdriver.Chrome(service=ser, options=op)
url = "https://registro.br/"
driver.get(url)

#domains list to check
domains = ["roboscompython.com.br","udemy.com","google.com","aleia.com.br", "strauusss.com"]
for domain in domains:
    search = driver.find_element(By.ID, "is-avail-field")
    search.clear()  # Cleaning the search bar
    search.send_keys(domain)
    search.send_keys(Keys.RETURN)
    time.sleep(2) #time to load the page
    #find information with a Tag
    results = driver.find_elements(By.TAG_NAME,"strong")
    # method to stop the code and trace the results by results[i].text. (c + enter closes it)
    #import pdb; pdb.set_trace()
    #print results
    print("Domain %s %s" % (domain, results[4].text))

driver.close()