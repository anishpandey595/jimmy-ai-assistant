import psutil
# get cpu usage
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent
# this function is used to convert text to speech
import pyttsx3
def say(text):
    eng = pyttsx3.init()  # initialize an instance
    voice = eng.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[2].id)  # changing voice to index 1 for heeraM and 2 for zira  female voice
    eng.say(text)
    eng.runAndWait()  # run and process the voice command
# this function is used to recognize voice command
import speech_recognition as sr
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=3)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f" User said: {query}")
            return query
        except Exception as e:
            return " "
# function for setting a remainder
import winsound
import time

def set_reminder():
    time_in_seconds = takecommand()
    print("Setting reminder for", time_in_seconds, "seconds")
    say("Setting reminder for", time_in_seconds , "seconds")
    message = takecommand()
    print("Reminder:", message)
    say("Reminder:", message)
    time.sleep(time_in_seconds)
    print("Reminder:", message)
    winsound.Beep(2500, 1000)  # Play a sound to grab attention

# this function is used to get weather of a particular city
import requests
def weather():
    print("please tell me the city name")
    say("please tell me the city name")
    city = takecommand()
    def get_weather(city):
        key = weather_key
        url = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + city + "&aqi=no&lang=en&alerts=yes"
        response = requests.get(url)
        return response.json()
    name = get_weather(city)["location"]["name"]
    temp_c = get_weather(city)["current"]["temp_c"]
    #    wind_kph = get_weather(city)["current"]["wind_kph"]
    #   humidity = get_weather(city)["current"]["humidity"]
    feelslike_c = get_weather(city)["current"]["feelslike_c"]
    condition = get_weather(city)["current"]["condition"]["text"]
    a = ("waeather in", name, "temp is ", temp_c, "degree in celcius", "feels like ",
         feelslike_c, "degree in celcius", "and condition is", condition)
    say(a)