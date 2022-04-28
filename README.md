# work_bot

![Badge](http://img.shields.io/static/v1?label=STATUS&message=UPDATING&color=BRIGHTGREEN&style=for-the-badge)

![Python](http://img.shields.io/static/v1?label=Python&message=v3.10&color=blue)
![Excel](http://img.shields.io/static/v1?label=Microsoft&message=Excel&color=blue)
![CHROMEDRIVER](http://img.shields.io/static/v1?label=Chromedriver&message=v100.0.4896.127&color=blue)


Bots designed for automation methods with Python.

## List of bots:
- Domains Availability Check:
    1. With a list of domains
       - can be found in /Bots/domainsCheck.py
    2. With external Excel file and saving results in another text file
       - can be found in /Bots/domainsCheckExcel.py
- Google bot
  - can be found in /Bots/googleBot.py
- Email bot:
  - Gmail server bot
    - can be found in /Bots/gmailBotServer.py
- Youtube bot
    - can be found in /Bots/youtubeBot.py
- Telegram bot
  - can be found in /Bots/telegramBot.py

## Bots to do:
- [x] Google bot[^1]
- [ ] Email bot
  - [x] Gmail server bot[^2]
  - [ ] With browser[^3]
- [x] Youtube bot[^4]
- [x] Telegram bot[^5]
- [ ] Audiobook bot

For the Telegram bot, create an API code in "https://my.telegram.org/" and add your information in the code /Bots/configTlgBot.py

## Deprecated mode changed:

PATH = 'C:/chromedriver'  
driver = webdriver.Chrome(PATH) <br>
driver.get(url)

## Clean mode:

ser = Service( )[^6]  
op = webdriver.ChromeOptions()  
#option to remove bluetooth adapter error     
op.add_experimental_option("excludeSwitches", ["enable-logging"])    
driver = webdriver.Chrome(service=ser, options=op)    
url = "website path"           
driver.get(url)

[^1]: Issues in getting all the links.
[^2]: Going to be deprecated soon with gmail changes.
[^3]: Starting soon.
[^4]: Minor issue in last page change.
[^5]: Only the option to add members. More options to implement later.
[^6]: With the chromedriver file on same folder you can leave the Service( ) parenthesis blank 
