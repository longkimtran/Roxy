# Some libraries use in AV
import os
import random
import subprocess
import webbrowser
from datetime import date, datetime

import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
import screen_brightness_control as sbc

from Data_Roxie import hello, google, end, unknown, thanks, voice1, web_data, intro
from Data_Roxie2 import water1, food_monday, food_friday, food_tuesday, \
    food_sunday, food_saturday, food_thursday, food_wednesday, wei1, wei2, wei3, activity1


def Roxie1(self):
    ai_hear = sr.Recognizer()
    ai_hear_1 = sr.Recognizer()
    ai_mouth = pyttsx3.init()

    while True:
        with sr.Microphone() as mic:  # Use micro in system
            print("Roxie: I'm hearing !")
            self.uic.Roxy_Talk.append("Roxie: I'm hearing !")
            audio = ai_hear.listen(mic, timeout=6,
                                   phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear.recognize_google(audio)
                print("You: " + me)
                self.uic.Roxy_Talk.append("You: " + me)

            except:
                me = "I cannot recognize your voice."
                print("You: " + me)
                self.uic.Roxy_Talk.append("Roxie: " + me)

            # SAY HELLO:
            if "hello" in me:
                ai_brain = str(random.choice(hello))

            # KNOWING ME:
            elif "know" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: Who are you?")
                    self.uic.Roxy_Talk.append("Roxie: Who are you?")
                    audio = ai_hear.listen(mic, timeout=6,
                                           phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)
                except:
                    me = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                ai_brain = "Oh hello " + me + " my master!"

            # INTRODUCTION OF ROXY:
            elif "who" in me or "introduce" in me:
                ai_brain = str(intro)

            # DAY IN CURRENT:
            elif "day" in me:
                today = date.today()  # use current date real life
                ai_brain = today.strftime("%B %d, %Y")

            # TIME IN CURRENT:
            elif "time" in me:
                now = datetime.now()
                ai_brain = now.strftime("%H:%M:%S")

            # ALTER VOLUME UP-DOWN-MUTE:
            elif "volume up" in me:
                pyautogui.press("volumeup")  # volume up in system
                ai_brain = "Ok, volume up!"

            elif "volume down" in me:
                pyautogui.press("volumedown")  # volume down in system
                ai_brain = "Ok, volume down!"

            elif "volume mute" in me or "mute" in me:
                pyautogui.press("volumemute")  # mute volume in system
                ai_brain = "Ok, mute volume !"

            # ALTER BRIGHTNESS ON SCREEN:
            elif "brightness up" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: How much brightness increase is appropriate, sir? ")
                    self.uic.Roxy_Talk.append("Roxie: How much brightness increase is appropriate, sir?")
                    audio = ai_hear.listen(mic, timeout=6,
                                           phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                except:
                    me = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                sbc.set_brightness(me, display=0)  # set brightness up in system
                ai_brain = "Ok, brightness up in " + str(me) + "% !"

            elif "brightness down" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: How much brightness reduction is appropriate, sir? ")
                    audio = ai_hear.listen(mic, timeout=6,
                                           phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)
                except:
                    me = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                sbc.set_brightness(me, display=0)  # set brightness down in system
                ai_brain = "Ok, brightness down in " + str(me) + "% !"

            # TEMPERATURE:
            elif "temperature" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: What are you looking for sir?")
                    self.uic.Roxy_Talk.append("Roxie: What are you looking for sir?")
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    temp = ai_hear_1.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)
                except:
                    temp = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                url = f"https://www.google.com/search?q={temp}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                # Web Scraping Values on Google Search Results
                temp2 = data.find("div", class_='BNeawe').text
                ai_brain = "The " + temp + " is " + temp2

            # OPENING WEBSITE:
            elif "Google" in me:
                ai_brain = str(random.choice(google))
                webbrowser.open('https://www.google.com.vn/')

            # ENTERTAINMENT APP:
            elif "entertainment" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: How do you want to entertain?")
                    self.uic.Roxy_Talk.append("Roxie: How do you want to entertain?")
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear_1.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)
                except:
                    me = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

                if "website" in me:
                    ai_brain = str(random.choice(voice1))
                    webbrowser.open(random.choice(web_data))

                elif "music" in me:
                    subprocess.call(r'C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe')
                    ai_brain = str(random.choice(voice1))

                elif "game" in me:
                    with sr.Microphone() as mic:  # Use micro in system
                        print("Roxie: What do you want game? ")
                        self.uic.Roxy_Talk.append("Roxie: What do you want game?")
                        audio = ai_hear_1.listen(mic, timeout=6,
                                                 phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                    print("Roxie:....")
                    try:
                        me = ai_hear_1.recognize_google(audio)
                        print("You: " + me)
                        self.uic.Roxy_Talk.append("You: " + me)
                    except:
                        me = "Something wrong here!"
                        print("You: " + me)
                        self.uic.Roxy_Talk.append("You: " + me)

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

            # CLOSE ALL TAB ON WEBSITE:
            elif "close" in me or "turn off" in me:
                ai_brain = str(random.choice(voice1))
                os.system("taskkill /im chrome.exe /f")

            # HEAL-CARE:
            elif "healthy" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: What do you need me to do sir? ")
                    self.uic.Roxy_Talk.append("You: " + me)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear_1.recognize_google(audio)
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)
                except:
                    me = "Something wrong here!"
                    print("You: " + me)
                    self.uic.Roxy_Talk.append("You: " + me)

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
                    ai_brain = "Please enter your weight and height, sir!"
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

            # SEARCHING INFORMATION:
            elif "searching" in me or "information" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: What are you looking for sir? ")
                    self.uic.Roxy_Talk.append("Roxie: What are you looking for sir? ")
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    info = ai_hear_1.recognize_google(audio)
                    print("You: " + info)
                    self.uic.Roxy_Talk.append("You: " + info)
                except:
                    info = "Something wrong here!"
                    print("You: " + info)
                    self.uic.Roxy_Talk.append("You: " + info)

                wikipedia.set_lang("en")
                ai_brain = wikipedia.summary(info, sentences=8)

            # QUIT:
            elif "bye" in me or "see" in me:
                ai_brain = str(random.choice(end))

                print("Roxie: " + ai_brain)
                self.uic.Roxy_Talk.append("Roxie: " + ai_brain)
                voices = ai_mouth.getProperty('voices')
                ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
                ai_mouth.say(ai_brain)
                ai_mouth.runAndWait()
                break

            # SAY THANKS YOU:
            elif "thank" in me or "thanks" in me:
                ai_brain = str(random.choice(thanks))

            # ANOTHER KEYS:
            else:
                if "about" in me:
                    ai_brain = "I'm fine thanks! So what do you want me do Sir?"
                else:
                    ai_brain = str(random.choice(unknown))

            print("Roxie: " + ai_brain)
            voices = ai_mouth.getProperty('voices')
            self.uic.Roxy_Talk.append("Roxy: " + str(ai_brain))
            ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
            ai_mouth.say(ai_brain)
            ai_mouth.runAndWait()
