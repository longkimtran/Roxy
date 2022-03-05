# Some libraries use in AV
import os
import random
import subprocess
import webbrowser
from datetime import date, datetime

import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

from Data_Roxie import hello, google, end, unknown, thanks, voice1, web_data
from Data_Roxie2 import water1, food_monday, food_friday, food_tuesday, \
    food_sunday, food_saturday, food_thursday, food_wednesday, wei1, wei2, wei3, activity1


def Roxie1():
    ai_hear = sr.Recognizer()
    ai_hear_1 = sr.Recognizer()
    ai_mouth = pyttsx3.init()

    while True:
        with sr.Microphone() as mic:  # Use micro in system
            print("Roxie: I'm hearing !")
            audio = ai_hear.listen(mic, timeout=6, phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

        print("Roxie:....")
        try:
            me = ai_hear.recognize_google(audio)
        except:
            me = "Something wrong here!"

        print("You: " + me)

        if "hello" in me:
            ai_brain = str(random.choice(hello))

        elif "day" in me:
            today = date.today()  # use current date real life
            ai_brain = today.strftime("%B %d, %Y")

        elif "time" in me:
            now = datetime.now()
            ai_brain = now.strftime("%H:%M:%S")

        elif "temperature" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: What are you looking for sir? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                temp = ai_hear_1.recognize_google(audio)
            except:
                temp = "Something wrong here!"
            print("You: " + temp)

            url = f"https://www.google.com/search?q={temp}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            # Web Scraping Values on Google Search Results
            temp2 = data.find("div", class_='BNeawe').text
            ai_brain = "The " + temp + " is " + temp2

        elif "Google" in me:
            ai_brain = str(random.choice(google))
            webbrowser.open('https://www.google.com.vn/')

        elif "entertainment" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: How do you want to entertain? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear_1.recognize_google(audio)
            except:
                me = "Something wrong here!"

            print("You: " + me)

            if "website" in me:
                ai_brain = str(random.choice(voice1))
                webbrowser.open(random.choice(web_data))

            elif "music" in me:
                subprocess.call(r'C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe')
                ai_brain = str(random.choice(voice1))

            elif "game" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: What do you want game? ")
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear_1.recognize_google(audio)
                except:
                    me = "Something wrong here!"

                print("You: " + me)
                if "Steam" in me or "steam" in me:
                    ai_brain = str(random.choice(voice1))
                    # subprocess.call() will help open fil in your pc or lap
                    subprocess.call(r'C:\Program Files (x86)\Steam\steam.exe')

                elif "Garena" in me or "garena" in me:
                    ai_brain = str(random.choice(voice1))
                    subprocess.call(r'C:\Program Files (x86)\Garena\Garena\Garena.exe')

                elif "Valorant" in me or "valorant" in me:
                    ai_brain = str(random.choice(voice1))
                    subprocess.call(r'D:\playgame\Riot Games\Riot Client\RiotClientServices.exe')
                else:
                    ai_brain = "Your game is not available or not installed sir!"

            else:
                ai_brain = "No application you want sir. Try again!"

        elif "close" in me or "turn off" in me:
            ai_brain = str(random.choice(voice1))
            os.system("taskkill /im chrome.exe /f")

        elif "healthy" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: What do you need me to do sir? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear_1.recognize_google(audio)
            except:
                me = "Something wrong here!"
            print("You: " + me)

            if "water" in me:
                ai_brain = str(water1)
            elif "eat" in me or "food" in me:
                curr_date = datetime.today().strftime('%A')
                if curr_date == "Monday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_monday)
                elif curr_date == "Tuesday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_tuesday)
                elif curr_date == "Wednesday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_wednesday)
                elif curr_date == "Thursday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_thursday)
                elif curr_date == "Friday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_friday)
                elif curr_date == "Saturday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_saturday)
                elif curr_date == "Sunday":
                    ai_brain = "Today is " + curr_date + ", " + str(food_sunday)

            elif "BMI" in me or "weight" in me:
                print("Please enter your weight and height, sir!")
                weight = float(input("Enter your weight(kg):  "))
                height = float(input("Enter your height(meter): "))

                print("Roxy: Calculating...!")

                bmi = weight / (height ** 2)

                if bmi <= 18.5:
                    ai_brain = "Your BMI is " + str(round(bmi, 2)) + ". You underweight, sir! " + str(wei1)

                elif 18.5 < bmi < 24.9:
                    ai_brain = "Your BMI is " + str(round(bmi, 2)) + ". " + str(wei2)

                elif 25 <= bmi < 34.9:
                    ai_brain = "Your BMI is " + str(round(bmi, 2)) + ". You overweight, sir! " + str(wei3) + \
                               str(random.choice(activity1))

                elif bmi >= 35:
                    ai_brain = "Your BMI is " + str(round(bmi, 2)) + ". You obese, sir! " + str(wei3) + \
                               str(random.choice(activity1))

            else:
                ai_brain = "You should follow the instructions of this menu to stay healthy, sir!"

        elif "searching" in me or "information" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: What are you looking for sir? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                info = ai_hear_1.recognize_google(audio)
            except:
                info = "Something wrong here!"
            print("You: " + info)

            wikipedia.set_lang("en")
            ai_brain = wikipedia.summary(info, sentences=8)

        elif "bye" in me or "see" in me:
            ai_brain = str(random.choice(end))

            print("Roxie: " + ai_brain)
            voices = ai_mouth.getProperty('voices')
            ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
            ai_mouth.say(ai_brain)
            ai_mouth.runAndWait()
            break

        elif "thank" in me or "thanks" in me:
            ai_brain = str(random.choice(thanks))

        else:
            if "about" in me:
                ai_brain = "I'm fine thanks! So what do you want me do Sir?"
            else:
                ai_brain = str(random.choice(unknown))

        print("Roxie: " + ai_brain)
        voices = ai_mouth.getProperty('voices')
        ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
