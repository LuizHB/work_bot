from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print("Iniciando nosso robô...\n")

'''    Depreciado (jeito mais direto)
PATH = 'C:/Users/Pc/Desktop/Luiz/Robos/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://registro.br/")
'''

#modo mais "bonito" e mais enxuto
ser = Service('C:/Users/Pc/Desktop/Luiz/Robos/chromedriver')
op = webdriver.ChromeOptions()
#opção para retirar o erro de adaptador de bluetooth
op.add_experimental_option("excludeSwitches", ["enable-logging"]) 

driver = webdriver.Chrome(service=ser, options=op)

url = "https://registro.br/"
driver.get(url)

pesquisa = driver.find_element(By.ID,"is-avail-field")
pesquisa.clear() #Limpando a barra de pesquisa
dominio = "roboscompython.com.br"
pesquisa.send_keys(dominio)

pesquisa.send_keys(Keys.RETURN)
time.sleep(2) #tempo para carregar a pagina

resultados = driver.find_elements(By.TAG_NAME,"strong")

#import pdb; pdb.set_trace() #parar o codigo para olhar os resultados usando: resultados[i].text e procurar o que precisa. Neste caso o 4 retorna disponivel e não disponivel. E para fechar o pdb só digitar c e apertar enter

print("Domínio %s %s" % (dominio, resultados[4].text))

time.sleep(4) #Conclusão
driver.close()