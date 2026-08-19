import psutil
import pyttsx3
import speech_recognition as sr
import winsound
import time
import requests

# Get CPU usage
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

# Text-to-speech function
def say(text):
    eng = pyttsx3.init()  
    voice = eng.getProperty('voices')  
    eng.setProperty('voice', voice[2].id)  # Zira female voice
    eng.say(text)
    eng.runAndWait()  

# Voice recognition function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return ""

# Reminder function (Fixed string formatting and error handling)
def set_reminder():
    say("How many seconds should I wait for the reminder?")
    time_input = takecommand()
    print(f"Heard time: {time_input}")
    
    try:
        # Attempt to convert spoken words/numbers into an integer
        time_in_seconds = int(''.join(filter(str.isdigit, time_input)))
    except ValueError:
        say("Sorry, I could not understand the time. Please try again.")
        return

    say(f"Setting reminder for {time_in_seconds} seconds.")
    
    say("What is the reminder message?")
    message = takecommand()
    print(f"Reminder message: {message}")
    
    say(f"Okay, I will remind you about: {message}")
    time.sleep(time_in_seconds)
    
    print(f"Reminder Alert: {message}")
    say(f"Reminder Alert: {message}")
    winsound.Beep(2500, 1000)  # Play a sound to grab attention

# Weather function (Fixed API key variable scope)
def weather(weather_api_key):
    say("Please tell me the city name.")
    city = takecommand()
    
    if not city.strip():
        say("I did not catch the city name.")
        return

    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no&lang=en&alerts=yes"
        response = requests.get(url)
        data = response.json()
        
        name = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        feelslike_c = data["current"]["feelslike_c"]
        condition = data["current"]["condition"]["text"]
        
        weather_report = f"Weather in {name}. Temperature is {temp_c} degrees Celsius, feels like {feelslike_c} degrees, and conditions are {condition}."
        print(weather_report)
        say(weather_report)
    except Exception as e:
        print(f"Error fetching weather: {e}")
        say("Sorry, I was unable to retrieve the weather data.")
