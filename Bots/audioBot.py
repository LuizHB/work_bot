import pyttsx3
import PyPDF2
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from tkinter import Tk
Tk().withdraw()
filelocation = askopenfilename(initialdir="C:\\Users\\Pc\\Desktop\\Luiz\\Robos\\Aulas\\audio_book\\audio_book", title="open file", filetypes=(("document", "*.pdf"),("document","*.*")))# Escolher arquivo com GUI

book = open(filelocation, 'rb')
print(book.read())

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("No. of pages: ", pages)
speaker = pyttsx3.init()
whole_text = '' # Armazena todos os textos
choice = input('Percorrer até que página? ')

for num in range(0, int(choice)):
    page = pdfReader.getPage(num)
    text = page.extractText()
    whole_text += text
    speaker.say(text)
    print("Lendo: ", text)
    speaker.runAndWait()


final_file = gTTS(text=whole_text, lang='pt')
name = input("Digite o nome do texto a ser salvo: ")
final_file.save( name+".mp3")  # Salvar arquivo mp3

book.close()
