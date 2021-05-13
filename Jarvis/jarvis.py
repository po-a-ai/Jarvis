import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning user I am Jarvis what can I do for you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon user I am Jarvis what can I do for you")
    else:
        speak("Good Evening user I am Jarvis what can I do for you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def quit():
    speak("Quitting all systems")
    speak("Closing Jarvis")
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(f'{query}', sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'turn off' in query:
            quit()
            break
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(time)
        elif 'open code' in query:
            os.startfile("C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'open zoom' in query:
            os.startfile("C:\\Users\\Acer\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")