# Some libraries use in AV
import speech_recognition as sr
import pyttsx3
from Roxie import Roxie1  # get function Roxie1 from Roxie.py
from Roxie_vn import Roxie2  # get function Roxie1 from Roxie_vn.py

ai_hear = sr.Recognizer()
ai_hear_1 = sr.Recognizer()
ai_mouth = pyttsx3.init()
ai_brain = ""

while True:
    with sr.Microphone() as mic:  # Use micro in system
        print("Roxie: Which languages you choose!")
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
