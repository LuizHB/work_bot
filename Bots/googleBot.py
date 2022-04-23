from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

print("Initiating the bot...\n")

search = input("What are you searching? ")

#webdriver - chromedriver version 100.0.4896.127
ser = Service()
op = webdriver.ChromeOptions()
#option to remove bluetooth adapter error
op.add_experimental_option("excludeSwitches", ["enable-logging"]) 
driver = webdriver.Chrome(service=ser, options=op)
url = "https:www.google.com.br"
driver.get(url)

searchBar = driver.find_element(By.XPATH,"//input[@aria-label='Pesquisar']")
searchBar.send_keys(search)
searchBar.send_keys(Keys.ENTER)

results = driver.find_element(By.XPATH,"//*[@id='result-stats']").text
print(results)
num_results = int(results.split("Aproximadamente ")[1].split(' resultados')[0].replace(".",""))
num_max_pages = num_results/10
target_page = input("%s number of pages found, till which one you wanna go? " % num_max_pages)

url_page = driver.find_element(By.XPATH,"//a[@aria-label='Page 2']").get_attribute("href")

actual_page = 0
start = 10
list_results = []
while actual_page <= int(target_page)-1:
    if actual_page >1:
        url_page = url_page.replace("start=%s" % start, "start=%s" % (start+10))
        start += 10
        driver.get(url_page)
    elif actual_page ==1:
        driver.get(url_page)
    actual_page += 1
    print("PAGE " + str(actual_page))

    divs = driver.find_elements(By.XPATH,"//div[@class='g']")
    for div in divs:
        name = div.find_element(By.TAG_NAME,"span")
        link = div.find_element(By.TAG_NAME,"a")
        result = "%s;%s" % (name.text,link.get_attribute("href"))
        print(result)
        list_results.append(result)


with open("Files/resultsGoogle.txt","w") as file:
    for result in list_results:
        file.write("%s \n" % result)
    file.close()

print("%s results found on Google and saved on resultsGoogle.txt" % len(list_results))

driver.close()