import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import pyautogui
import time
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis. How may I help you??")


def jokes():
    joker = pyjokes.get_joke()
    print(joker)
    speak(joker)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_ratio = 0.2
        r.energy_threshold = 5
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
    except Exception as e:
        # print(e)
        print("Sorry, can you repeat it again??? ")
        return "None"
    return query

def edge_google():
    
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    os.startfile(edge_path)

    time.sleep(5.0)

    site = "https://www.google.co.in/"

    for word in site:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        break

def edge_youtube():
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    os.startfile(edge_path)

    time.sleep(6.0)

    # site1 = "https://www.youtube.com/"

    for word1 in open("yt", "r"):
        pyautogui.typewrite(word1)
        pyautogui.press("enter")
        break

def edge_stckovf():
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    os.startfile(edge_path)

    time.sleep(6.0)

    # site1 = "https://www.youtube.com/"

    for word1 in open("st", "r"):
        pyautogui.typewrite(word1)
        pyautogui.press("enter")
        break


if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in query:
            edge_youtube()

        elif "open stackoverflow" in query:
            edge_stckovf()

        elif "play songs" in query:
            music_dir = "E:\\devansh\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%date:%h:%m:%S")
            speak(f"Sir, the time is {strTime}")

        elif "good" in query:
            speak("Thank you for your compliment!!")

        elif "bad" in query:
            speak("Sorry you feel bad..."
                  "How shall I improve myself??")

        elif "open telegram" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Telegram\\Telegram.exe"
            os.startfile(codePath)

        elif "quit" in query:
            exit()

        elif "bye" in query:
            exit()
        
        elif "open google" in query:
            edge_google()
        
        elif "joke" in query:
            jokes()