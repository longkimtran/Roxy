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
import wmi

import Global
from Data_Roxie import hello, google, end, unknown, thanks, voice1, web_data, intro
from Data_Roxie2 import water1, food_monday, food_friday, food_tuesday, \
    food_sunday, food_saturday, food_thursday, food_wednesday, wei1, wei2, wei3, activity1


def Roxie1(self):
    ai_hear = sr.Recognizer()
    ai_hear_1 = sr.Recognizer()
    ai_mouth = pyttsx3.init()

    while True:
        with sr.Microphone() as mic:  # Use micro in system
            Global.machine_text(self, Global.MACHINE_WAITING_1)
            audio = ai_hear.listen(mic, timeout=6,
                                   phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            try:
                me = ai_hear.recognize_google(audio)
                Global.user_text(self, me)

            except:
                me = "I cannot recognize your voice."
                Global.machine_text(self, me)

            # SAY HELLO:
            if "hello" in me:
                ai_brain = str(random.choice(hello))

            # KNOWING ME:
            elif "know" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_KNOWING)
                    audio = ai_hear.listen(mic, timeout=6,
                                           phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    me = ai_hear.recognize_google(audio)
                    Global.user_text(self, me)
                except:
                    me = "Something wrong here!"
                    Global.machine_text(self, me)

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
            elif "brightness" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_CONTROL_BRIGHTNESS)
                    audio = ai_hear.listen(mic, timeout=6,
                                           phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    me = ai_hear.recognize_google(audio)
                    Global.user_text(self, me)

                except:
                    me = "Something wrong here!"
                    Global.machine_text(self, me)

                c = wmi.WMI(namespace='wmi')
                methods = c.WmiMonitorBrightnessMethods()[0]
                ai_brain = "Ok, Brightness is adjusted at " + me + "% !"
                methods.WmiSetBrightness(me, 0)

            elif "temperature" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_TEMPERATURE)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    temp = ai_hear_1.recognize_google(audio)
                    Global.user_text(self, temp)
                except:
                    temp = "Something wrong here!"
                    Global.user_text(self, temp)

                url = f"https://www.google.com/search?q={temp}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                # Web Scraping Values on Google Search Results
                temp2 = data.find("div", class_='BNeawe').text
                ai_brain = "The " + temp + " is " + temp2 + " sir!"

            # OPENING WEBSITE:
            elif "Google" in me:
                ai_brain = str(random.choice(google))
                webbrowser.open('https://www.google.com.vn/')

            # ENTERTAINMENT APP:
            elif "entertainment" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_ENTERTAINMENT)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    me = ai_hear_1.recognize_google(audio)
                    Global.user_text(self, me)
                except:
                    me = "Something wrong here!"
                    Global.user_text(self, me)

                if "website" in me:
                    ai_brain = str(random.choice(voice1))
                    webbrowser.open(random.choice(web_data))

                elif "music" in me:
                    subprocess.call(r'C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe')
                    ai_brain = str(random.choice(voice1))

                elif "game" in me:
                    with sr.Microphone() as mic:  # Use micro in system
                        Global.machine_text(self, Global.MACHINE_GAME)
                        audio = ai_hear_1.listen(mic, timeout=6,
                                                 phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                    try:
                        me = ai_hear_1.recognize_google(audio)
                        Global.user_text(self, me)
                    except:
                        me = "Something wrong here!"
                        Global.user_text(self, me)

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
                    Global.machine_text(self, Global.MACHINE_HEALTH_CARE)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    me = ai_hear_1.recognize_google(audio)
                    Global.user_text(self, me)
                except:
                    me = "Something wrong here!"
                    Global.user_text(self, me)

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
                    """with sr.Microphone() as mic:  # Use micro in system
                        Global.machine_text(self, Global.MACHINE_HEALTH_CARE_BMI_WEIGHT)
                        audio = ai_hear_1.listen(mic, timeout=6,
                                                 phrase_time_limit=3)  # let the computer listen for exactly 3 seconds
                    try:
                        weight = ai_hear_1.recognize_google(audio)
                        Global.user_text(self, weight)

                    except:
                        weight = "Something wrong here!"
                        Global.user_text(self, weight)

                    with sr.Microphone() as mic:  # Use micro in system
                        Global.machine_text(self, Global.MACHINE_HEALTH_CARE_BMI_HEIGHT)
                        audio = ai_hear_1.listen(mic, timeout=6,
                                                 phrase_time_limit=3)  # let the computer listen for exactly 3 seconds
                    try:
                        height = ai_hear_1.recognize_google(audio)
                        Global.user_text(self, height)

                    except:
                        height = "Something wrong here!"
                        Global.user_text(self, height)"""

                    weight = float(input("Enter your weight: "))
                    Global.user_text(self, weight + "kg")
                    height = float(input("Enter your height: "))
                    Global.user_text(self, height + "meter")

                    Global.machine_text(self, "Calculating....")

                    bmi = float(weight) / float((height ** 2))

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

            # ALARM CLOCK:
            elif "set" in me:
                def validate_time(awake_time):
                    if len(awake_time) != 11:
                        err = "Invalid time format! Please try again..."
                        Global.machine_text(self, err)
                    else:
                        if int(awake_time[0:2]) > 12:
                            err1 = "Invalid HOUR format! Please try again..."
                            Global.machine_text(self, err1)
                        elif int(awake_time[3:5]) > 59:
                            err2 = "Invalid MINUTE format! Please try again..."
                            Global.machine_text(self, err2)
                        elif int(awake_time[6:8]) > 59:
                            err3 = "Invalid SECOND format! Please try again..."
                            Global.machine_text(self, err3)
                        else:
                            return "ok"

                while True:
                    awake_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

                    validate = validate_time(awake_time.lower())
                    if validate != "ok":
                        print(validate)
                    else:
                        Global.user_text(self, awake_time)

                        ai_brain3 = "Ok I'll wake you up at " + awake_time + ", sir!"

                        voices = ai_mouth.getProperty('voices')
                        Global.machine_text(self, ai_brain3)
                        ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
                        ai_mouth.say(ai_brain3)
                        ai_mouth.runAndWait()
                        break

                alarm_hour = awake_time[0:2]
                alarm_min = awake_time[3:5]
                alarm_sec = awake_time[6:8]
                alarm_period = awake_time[9:].upper()

                while True:
                    now = datetime.now()

                    current_hour = now.strftime("%I")
                    current_min = now.strftime("%M")
                    current_sec = now.strftime("%S")
                    current_period = now.strftime("%p")

                    if alarm_period == current_period:
                        if alarm_hour == current_hour:
                            if alarm_min == current_min:
                                if alarm_sec == current_sec:
                                    ai_brain = "Time to wake-up sir!, Time to wake-up sir!, Time to wake-up sir!, " \
                                               "Time to wake-up sir!, Time to wake-up sir!, Time to wake-up sir! "
                                    break

            # SEARCHING INFORMATION:
            elif "searching" in me or "information" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_INFORMATION)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds
                try:
                    info = ai_hear_1.recognize_google(audio)
                    Global.user_text(self, info)
                except:
                    info = "Something wrong here!"
                    Global.user_text(self, info)

                wikipedia.set_lang("en")
                ai_brain = wikipedia.summary(info, sentences=8)

            # QUIT:
            elif "bye" in me or "see" in me:
                ai_brain = str(random.choice(end))

                Global.machine_text(self, ai_brain)
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

            voices = ai_mouth.getProperty('voices')
            Global.machine_text(self, ai_brain)
            ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)
            ai_mouth.say(ai_brain)
            ai_mouth.runAndWait()
