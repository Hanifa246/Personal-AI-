import datetime
import os
import pyttsx3
import speech_recognition as sr
import webbrowser



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        return "Sorry, I couldn't understand that."


if __name__ == '__main__':
    print("PyCharm")
    say("Hello, I am Mufassal.")

    while True:
        print("Listening...")
        query = takeCommand()
        #todo : Add more sites
        sites = [["youtube","https://youtube.com"],
                 ["chatgpt","https://chatgpt.com"],
                 ["whatsapp","https://whatsapp.com"],
                 ["instagram","https://instagram.com"],
                 ["blackbox","https://blackbox.com"],
                 ["github","https://github.com"],
                 ["google","https://google.com"]]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} madam...")
                webbrowser.open(site[1])
# todo: Add a feature to play a specific song
        if "play music" in query:
            musicpath = r"C:\Users\91990\Downloads\Paro - PagalHits.mp3"
            os.startfile(musicpath)

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            say(f"sir the time is {hour} hours and {minutes} minutes")
        #say(query)
