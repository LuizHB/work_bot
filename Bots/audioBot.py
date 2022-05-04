import pyttsx3
import fitz
from gtts import gTTS
from tkinter import Tk

Tk().withdraw()
# Choose the file
book = fitz.open(r'\Files\Lorem_ipsum.pdf')
pages = book.page_count
print("No. of pages: ", pages)
#calling the speaker lib
speaker = pyttsx3.init()
# Get the whole text
whole_text = ''
choice = input('Go till which page? ')

#calling the text to read
for num in range(0, int(choice)):
    page = book.load_page(num)
    text = page.get_text("text")
    whole_text += text
    speaker.say(text)
    print("Reading: ", text)
    speaker.runAndWait()

#choose the language in 'lang'
#change tld to 'com' for english and lang to 'en'
final_file = gTTS(text=whole_text, lang='pt',tld="com.br")
name = input("Type the name of the file to be saved: ")
# Save file in mp3
final_file.save(r"\Files\%s.mp3" % name)

book.close()
