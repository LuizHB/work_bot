# work_bot

![Badge](http://img.shields.io/static/v1?label=STATUS&message=UPDATING&color=BRIGHTGREEN&style=for-the-badge)

![Python](http://img.shields.io/static/v1?label=Python&message=v3.10&color=blue)
![Excel](http://img.shields.io/static/v1?label=Microsoft&message=Excel&color=blue)
![CHROMEDRIVER](http://img.shields.io/static/v1?label=Chromedriver&message=v100.0.4896.127&color=blue)


Bots designed for automation methods with Python.

## List of bots:
- Domains Availability Check:
  - can be found in /Bots/domainsCheck.py
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

## Description of the bots
  
- Domains Availability Check:
   - The domainsCheck scans the availability of website domains With a list of domains and return the results in a list. The domainsCheckExcel reads the list of domains inside an Excel file and save the results in a text file.
- Google bot
  - The googleBot searches for determined information on Google website and return the results in a text file.
- Email bot:
  - The gmailBotServer apply the SMTP protocol client library to send emails using gmail server. There are options to attach files and external body text as such HTML codes. For the server bot is necessary to enable the option "Less secure app access" in Google account management security's tab. 
- YouTube bot
  - The youtubeBot searches for determined information on YouTube website and return the results inside the console.
- Telegram bot
  - The telegramBot applies a method combining telegram's API with telethon library to get the members of a group in telegram and add in another group. Other methods will be applied later. For this bot, create an API code in "https://my.telegram.org/" and add your information in the code found in /Bots/configTlgBot.py
- Audiobook bot
  - The audioBookBot convert a PDF file to audio in MP3 format.

## Bots to do:
- [x] Google bot[^1]
- [ ] Email bot
  - [x] Gmail server bot[^2]
  - [ ] With browser[^3]
- [x] Youtube bot[^4]
- [x] Telegram bot[^5]
- [ ] Audiobook bot[^6]

## Deprecated mode changed:

PATH = 'C:/chromedriver'  
driver = webdriver.Chrome(PATH) <br>
driver.get(url)

## Clean mode:

ser = Service( )[^7]  
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
[^6]: Starting soon.
[^7]: With the chromedriver file on same folder you can leave the Service( ) parenthesis blank 
