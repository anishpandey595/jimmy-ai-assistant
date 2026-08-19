import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from selenium.webdriver.common.by import By
ScriptDir = pathlib.Path().absolute()


url = "https://flowgpt.com/"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/000000000 Safari/537.36
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options) #chrome khola
sleep(1)
driver.maximize_window() #window ko maximaze kiya
driver.get(url =url) # link khola
sleep(500)# 10 sec badd close kar diya

def popupremover():
    #Xpath = '/html/body/div[3]/div[3]/div/section/button'
    popup = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/button')
    popup.click()

popupremover()
sleep(500)