import pyttsx3
import PyPDF2
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from tkinter import Tk
Tk().withdraw()
filelocation = askopenfilename(initialdir="C:\\Users\Pc\\Documents\\GitHub\\work_bot\\Bots\\Files", title="open file", filetypes=(("document", "*.pdf"),("document","*.*")))# Choose the file

book = open(filelocation, 'rb')
print(book.read())

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("No. of pages: ", pages)
speaker = pyttsx3.init()
whole_text = '' # Get the whole text
choice = input('Go till which page? ')

for num in range(0, int(choice)):
    page = pdfReader.getPage(num)
    text = page.extractText()
    whole_text += text
    speaker.say(text)
    print("Reading: ", text)
    speaker.runAndWait()


final_file = gTTS(text=whole_text, lang='pt')
name = input("Type the name of the file to be saved: ")
final_file.save( name+".mp3")  # Save file in mp3

book.close()
