import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#creating a class for the bot
class YoutubeRobot():
    #def to open the browser
    def __init__(self):
        self.webdriver = webdriver.Chrome()

    #def to search in the page
    def search(self, searching, pages):
        videos =[]
        page = 1
        url = "https://www.youtube.com/results?search_query=%s" % searching
        self.webdriver.get(url)

        #while function to separate already chosen videos
        while page <= pages:
            titles = self.webdriver.find_elements(By.XPATH, "//a[@id='video-title']")
            for title in titles:
                if title.text not in videos:
                    print("Video found: %s" % title.text)
                    videos.append(title.text)
            self.nextPage(page)
            page += 1

    #def to change the pages (useful if the method get changed)
    def nextPage(self, page):
        print("Changing to page %s" % (page +1))
        bottom = page *10000
        self.webdriver.execute_script("window.scrollTo(0,%s);" % bottom)
        time.sleep(3)
        pass

    #def to close the browser
    def closeBrowser(self):
        self.webdriver.close()

#script to call the bot and ask about the search
print("Initiating the bot...\n")
question = input("What are you searching for? ")
bot = YoutubeRobot()
bot.search(question,5)
bot.closeBrowser()

