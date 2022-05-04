import pyttsx3
import fitz
from gtts import gTTS
from tkinter import Tk

Tk().withdraw()
# Choose the file
book = fitz.open(r'C:\Users\Pc\Documents\GitHub\work_bot\Bots\Files\Lorem_ipsum.pdf')

pages = book.page_count
print("No. of pages: ", pages)
speaker = pyttsx3.init()
whole_text = ''  # Get the whole text
choice = input('Go till which page? ')

for num in range(0, int(choice)):
    page = book.load_page(num)
    text = page.get_text("text")
    whole_text += text
    speaker.say(text)
    print("Reading: ", text)
    speaker.runAndWait()

final_file = gTTS(text=whole_text, lang='pt')
name = input("Type the name of the file to be saved: ")
final_file.save(name + ".mp3")  # Save file in mp3

book.close()
