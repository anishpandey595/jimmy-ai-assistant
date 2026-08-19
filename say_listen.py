import pyttsx3
import speech_recognition as sr

def say(text):
    eng = pyttsx3.init()  # initialize an instance
    voice = eng.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[1].id)  # changing voice to index 1 for heeraM and 2 for zira  female voice
    eng.say(text)
    eng.runAndWait()  # run and process the voice command


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3,)
        try:
            query = r.recognize_google_cloud()
            print(f" User said: {query}")
            return query
        except Exception as e:
            return " "


a= takecommand()
say(a)