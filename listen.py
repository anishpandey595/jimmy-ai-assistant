# command = hindi or english
# result = english
# pip install googletrans==4.0.0rc1
import speech_recognition as sr
from googletrans import Translator
'''def TC_Hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="hi")
            print(f" User said: {query}")
            return query
        except Exception as e:
            return " some error ocurred"

# This code for translation english to hindi
def TransToHindi():
    print("Tell me the Line To Translate")
    line = TC_Hindi()
    traslate = Translator()
    result = traslate.translate(line, dest="en")
    print("translated line is:  " + result.text)

TransToHindi()'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "GoogleChromePortablef.exe"
driver = webdriver.Chrome(executable_path=Path, options=chrome_options)


driver.maximize_window()

