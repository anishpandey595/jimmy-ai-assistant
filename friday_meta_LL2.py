

import datetime
import speech_recognition as sr
import pyttsx3  # import the library
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
def say(text):
    eng = pyttsx3.init()  # initialize an instance
    voice = eng.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[2].id)  # changing voice to index 1 for heeraM and 2 for zira  female voice
    eng.say(text)
    eng.runAndWait()  # run and process the voice command
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("good morning sir... ")
    elif hour >= 12 and hour < 18:
        say("good afternoon sir...")
    else:
        say("good evening sir...")
def friday():
    import replicate
    import os
    os.environ["REPLICATE_API_TOKEN"] = "YOUR_API_KEY"

    wishme()
    say("friday is online")
    while True:
        query = takecommand()
        say(query)
        output = replicate.run(
            "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
            input={
                "prompt": query
            }
        )
        for item in output:
            # https://replicate.com/meta/llama-2-70b-chat/api#output-schema
            print(item, end="")
            say(item)
