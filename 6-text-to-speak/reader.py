import pyttsx3
import requests
from bs4 import BeautifulSoup

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('vice', voices[1].id)
engin.setProperty('rate', 145)
# text = str(input('enter text en to save mp3 file: '))

file = open("reader.txt", "a")
engin.save_to_file(file.read(), 'file.mp3')
engin.runAndWait()
