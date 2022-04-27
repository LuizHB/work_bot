# work_bot

![Badge](http://img.shields.io/static/v1?label=STATUS&message=UPDATING&color=BRIGHTGREEN&style=for-the-badge)

![Python](http://img.shields.io/static/v1?label=Python&message=v3.10&color=blue)
![Excel](http://img.shields.io/static/v1?label=Microsoft&message=Excel&color=blue)

Bots designed for automation methods with Selenium and Excel files.

## List of bots:
- Domains Availability Check
    1. With a list of domains
    2. With external Excel file and saving results in another text file

## Bots to do:
- [x] Google bot[^2]
- [ ] Email bot
  - [x] Gmail server bot[^3]
  - [ ] With browser[^4]
- [ ] Youtube bot
- [ ] Telegram bot


## Deprecated mode changed:

PATH = 'C:/chromedriver'  
driver = webdriver.Chrome(PATH) <br>
driver.get(url)

## Clean mode:

ser = Service( )[^1]  
op = webdriver.ChromeOptions()  
#option to remove bluetooth adapter error     
op.add_experimental_option("excludeSwitches", ["enable-logging"])    
driver = webdriver.Chrome(service=ser, options=op)    
url = "website"           
driver.get(url)

[^1]: With the chromedriver file on same folder you can leave the Service( ) parenthesis blank <br>
[^2]: Minor issues to fix later. <br>
[^3]: Going to be deprecated soon with gmail changes.<br>
[^4]: Starting soon