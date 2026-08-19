import pyttsx3
import speech_recognition as sr

def say(text):
    eng = pyttsx3.init()  # initialize an instance
    voice = eng.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[2].id)  # changing voice to index 1 for heeraM and 2 for zira  female voice
    eng.say(text)
    eng.runAndWait()  # run and process the voice command


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f" User said: {query}")
            return query
        except Exception as e:
            return " "

def MainExecution(query):
    Query = str(query).lower()

    if "hello" in Query:
        say("Hello Sir, Welcome Back!")

    elif "bye" in Query:
        say("Nice to meet you sir, Have a nice day!")

    elif "time" in Query:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        say(f"The Time Now Is : {time}")

    elif "bye" in Query:
        say("Nice to meet you sir, Have a nice day!")

    elif "bye" in Query:
        say("Nice to meet you sir, Have a nice day!")