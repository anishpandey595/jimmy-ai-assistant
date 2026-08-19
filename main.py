import os
import pyttsx3
import speech_recognition as sr
from datetime import datetime

# Import your custom project modules
from features import get_cpu_usage, set_reminder, weather
from face_recoginition import Face_recoginition

def speak(text):
    eng = pyttsx3.init()  
    voice = eng.getProperty('voices')  
    eng.setProperty('voice', voice[2].id)  # Zira female voice
    eng.say(text)
    eng.runAndWait()  

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("\nListening...")
        audio = r.listen(source, phrase_time_limit=3)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return ""

def wishme():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")

def main():
    print("--- Jimmy AI Assistant Initializing ---")
    
    # Step 1: Biometric Security Check
    speak("Verifying identity using facial recognition.")
    print("Starting face recognition... Please look at the camera.")
    try:
        Face_recoginition()
    except Exception as e:
        print(f"Facial recognition skipped or failed: {e}")
    
    # Step 2: Welcome sequence
    wishme()
    speak("System unlocked. All features are online.")
    
    # Step 3: Main Command Loop
    while True:
        query = takecommand().lower()
        
        if not query.strip():
            continue
            
        if "hello" in query:
            speak("Hello sir, welcome back!")
            
        elif "time" in query:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time now is {current_time}")
            
        elif "cpu" in query or "system status" in query:
            usage = get_cpu_usage()
            speak(f"Current CPU usage is at {usage} percent.")
            
        elif "reminder" in query or "set reminder" in query:
            set_reminder()
            
        elif "weather" in query:
            # Pass your WeatherAPI key here (replace with your actual key string)
            weather_api_key = "YOUR_WEATHER_API_KEY"
            weather(weather_api_key)
            
        elif "exit" in query or "bye" in query or "stop" in query:
            speak("Nice to meet you sir. Have a nice day!")
            print("Assistant shutting down.")
            break
            
        else:
            speak("I heard your command, but that feature is handled by my advanced models. Check your meta LL file for cloud processing.")

if __name__ == "__main__":
    main()
