# Some libraries use in AV
import datetime
from threading import Thread

import pyttsx3
import speech_recognition as sr

from Roxie import Roxie1  # get function Roxie1 from Roxie.py
from Roxie_vn import Roxie2  # get function Roxie1 from Roxie_vn.py
from Roxy_Interface import GifRoxy

ai_hear = sr.Recognizer()
ai_hear_1 = sr.Recognizer()
ai_mouth = pyttsx3.init()
ai_brain = ""


def wish():
    hour = int(datetime.datetime.now().hour)
    if 8 <= hour <= 12:
        ai_brain2 = "Good morning sir. I'm Roxy your virtual assistance. Please choose your language for you, sir!"
    elif 12 < hour < 18:
        ai_brain2 = "Good afternoon sir. I'm Roxy your virtual assistance. Please choose your language for you, sir!"
    else:
        ai_brain2 = "Good evening sir. I'm Roxy your virtual assistance. Please choose your language for you, sir!"

    print("Roxie: " + ai_brain2)
    voice = ai_mouth.getProperty('voices')
    ai_mouth.setProperty('voice', voice[1].id)  # voice AI: 0(Male), 1(Female)
    ai_mouth.say(ai_brain2)
    ai_mouth.runAndWait()


wish()

while True:
    with sr.Microphone() as mic:  # Use micro in system
        print("Roxie: I'm waiting !!!")
        audio = ai_hear.listen(mic, timeout=6, phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

    print("Roxie:....")
    try:
        me = ai_hear.recognize_google(audio)
    except:
        me = "Something wrong here!"
    print("You: " + me)

    if "English" in me:
        Roxie1()
        break
    elif "Vietnamese" in me:
        Roxie2()
        break
    else:
        ai_brain = "You not choose or something. Try again!"

    print("Roxie: " + ai_brain)
    voices = ai_mouth.getProperty('voices')
    ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()
