# work_bot

![Badge](http://img.shields.io/static/v1?label=STATUS&message=UPDATING&color=BRIGHTGREEN&style=for-the-badge)

![Python](http://img.shields.io/static/v1?label=Python&message=v3.10&color=blue)
![Excel](http://img.shields.io/static/v1?label=Microsoft&message=Excel&color=blue)
![CHROMEDRIVER](http://img.shields.io/static/v1?label=Chromedriver&message=v100.0.4896.127&color=blue)


Bots designed for automation methods with Python.

## List of bots:
- Domains Availability Check:
  - [domainsCheck](/Bots/domainsCheck.py)
  -  [domainsCheckExcel](/Bots/domainsCheckExcel.py)
- Google bot
  - [googleBot](/Bots/googleBot.py)
- Email bot:
  - Gmail server bot
    - [gmailServerBot](/Bots/gmailBotServer.py)
  - Browser bot
- Youtube bot
    - [youtubeBot](/Bots/youtubeBot.py)
- Telegram bot
  - [telegramBot](/Bots/telegramBot.py)
  - Script to run the bot: [run](/Bots/run.py)
  - Configuration file: [configTlgBot](/Bots/configTlgBot.py)
- Audio bot
  - [audioBot](/Bots/audioBot.py) 

## Description of the bots
  
- Domains Availability Check:
   - The [domainsCheck](/Bots/domainsCheck.py) scans the availability of website domains With a list of domains and return the results in a list. The [domainsCheckExcel](/Bots/domainsCheckExcel.py) reads the list of domains inside an Excel file and save the results in a text file.
- Google bot
  - The [googleBot](/Bots/googleBot.py) searches for determined information on Google website and return the results in a text file.
- Email bot:
  - The [gmailServerBot](/Bots/gmailBotServer.py) apply the SMTP protocol client library to send emails using gmail server. There are options to attach files and external body text as such HTML codes. For the server bot is necessary to enable the option "Less secure app access" in Google account management security's tab. 
- YouTube bot
  - The [youtubeBot](/Bots/youtubeBot.py) searches for determined information on YouTube website and return the results inside the console.
- Telegram bot
  - The [telegramBot](/Bots/telegramBot.py) applies a method combining telegram's API with telethon library to get the members of a group in telegram and add in another group. Other methods will be applied later. For this bot, create an API code in "https://my.telegram.org/" and add your information in the code found in [configTlgBot](/Bots/configTlgBot.py). To run this code, another script was made named [run](/Bots/run.py).
- Audio bot
  - The [audioBot](/Bots/audioBot.py) converts a PDF file to audio in MP3 format. A sample PDF file is found in Files folder.

## Bots to do:
- [x] Google bot[^1]
- [ ] Email bot
  - [x] Gmail server bot[^2]
  - [ ] With browser[^3]
- [x] Youtube bot[^4]
- [x] Telegram bot[^5]
- [x] Audiobook bot[^6]

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
[^6]: Might get errors with host connection depending on your internet connection.
[^7]: With the chromedriver file on same folder you can leave the Service( ) parenthesis blank 
