# Some libraries use in AV
import os
import random
import subprocess
import webbrowser
from datetime import date, datetime

import pyautogui
import requests
import speech_recognition as sr
import wikipedia
import wmi
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound

import Global
from Data_Roxie import hello_vn, google_vn, end_vn, unknown_vn, \
    thanks_vn, voice_vn1, web_data, intro_vn
from Data_Roxie3 import water2, food_friday_vn, food_monday_vn, food_saturday_vn, \
    food_sunday_vn, food_thursday_vn, food_tuesday_vn, food_wednesday_vn, activity2, wei1_vn, wei2_vn, wei3_vn


def Roxie2(self):
    ai_hear = sr.Recognizer()
    ai_hear_1 = sr.Recognizer()

    while True:
        with sr.Microphone() as mic:  # Use micro in system
            Global.machine_text(self, Global.MACHINE_WAITING_VN)
            audio = ai_hear.listen(mic, timeout=6,
                                   phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

        try:
            me = ai_hear.recognize_google(audio, language="vi-VN")
            Global.user_text(self, me)
        except:
            me = "Tôi không hiểu !"
            Global.machine_text(self, me)

        # SAY HELLO:
        if "Xin chào" in me or "Hello" in me or "Hi" in me:
            ai_brain = str(random.choice(hello_vn))

        # KNOWING ME:
        elif "tôi" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_KNOWING_VN)
                audio = ai_hear.listen(mic, timeout=6,
                                       phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear.recognize_google(audio, language="vi-VN")
                Global.user_text(self, me)
            except:
                me = "Có gì đó không đúng!"
                Global.machine_text(self, me)

            ai_brain = "Oh Xin chào " + me + ", chủ nhân của tôi!"

        # INTRODUCTION OF ROXY:
        elif "giới thiệu" in me or "ai" in me:
            ai_brain = str(intro_vn)

        # DAY IN CURRENT:
        elif "ngày" in me:
            today = date.today()  # use current date real life
            ai_brain = today.strftime("%d/%m/%Y")

        # TIME IN CURRENT:
        elif "giờ" in me:
            now = datetime.now()
            ai_brain = now.strftime("%H:%M:%S")

        # ALTER VOLUME UP-DOWN-MUTE:
        elif "tăng" in me:
            pyautogui.press("volumeup")  # volume up in system
            ai_brain = "Đã tăng âm lượng!"

        elif "giảm" in me:
            pyautogui.press("volumedown")  # volume down in system
            ai_brain = "Đã giảm âm lượng!"

        elif "tắt tiếng" in me or "mute" in me:
            pyautogui.press("volumemute")  # mute volume in system
            ai_brain = "Tắt tiếng!"

        # ALTER BRIGHTNESS ON SCREEN:
        elif ("điều chỉnh" in me and "độ sáng" in me) or "màn hình" in me or "độ sáng" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_CONTROL_BRIGHTNESS_VN)
                audio = ai_hear.listen(mic, timeout=6,
                                       phrase_time_limit=3)  # let the computer listen for exactly 3 seconds
            try:
                me = ai_hear.recognize_google(audio, language="vi-VN")
                Global.user_text(self, me)
            except:
                me = "Có gì đó không đúng!"
                Global.machine_text(self, me)

            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            ai_brain = "Độ sáng đươc điều chỉnh ở mức " + me + "% !"
            methods.WmiSetBrightness(me, 0)

        # TEMPERATURE:
        elif "nhiệt độ" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_TEMPERATURE_VN)
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            try:
                temp = ai_hear_1.recognize_google(audio, language="vi-VN")
                Global.user_text(self, temp)
            except:
                temp = "Có gì đó không đúng!"
                Global.machine_text(self, temp)

            url = f"https://www.google.com/search?q={temp}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            # Web Scraping Values on Google Search Results
            temp2 = data.find("div", class_='BNeawe').text
            ai_brain = temp + " là " + temp2 + " thưa ngài!"

        # OPENING WEBSITE:
        elif "Google" in me:
            ai_brain = str(random.choice(google_vn))
            webbrowser.open('https://www.google.com.vn/')

        # ENTERTAINMENT APP:
        elif "giải trí" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_ENTERTAINMENT_VN)
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds
            print("Roxie:....")

            try:
                me = ai_hear_1.recognize_google(audio, language="vi-VN")
                Global.user_text(self, me)
            except:
                me = "Có gì đó không đúng!"
                Global.machine_text(self, me)

            if "trình duyệt" in me:
                ai_brain = str(random.choice(voice_vn1))
                webbrowser.open(random.choice(web_data))

            elif "nhạc" in me:
                subprocess.call(r'C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe')
                ai_brain = str(random.choice(voice_vn1))

            elif "trò chơi" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    Global.machine_text(self, Global.MACHINE_GAME_VN)
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                try:
                    me = ai_hear_1.recognize_google(audio, language="vi-VN")
                    Global.user_text(self, me)
                except:
                    me = "Có gì đó không đúng!"
                    Global.machine_text(self, me)

                if "steam" in me or "Steam" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    # subprocess.call() will help open fil in your pc or lap
                    subprocess.call(r'C:\Program Files (x86)\Steam\steam.exe')

                elif "Garena" in me or "garena" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    subprocess.call(r'C:\Program Files (x86)\Garena\Garena\Garena.exe')

                elif "valorant" in me or "Valorant" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    subprocess.call(r'D:\playgame\Riot Games\Riot Client\RiotClientServices.exe')

                else:
                    ai_brain = "Trò chơi của ngài không tồn tại hoặc chưa cài đặt!"

            else:
                ai_brain = "Không có mục giải trí ngài cần. Hãy thử lại!"

        # CLOSE ALL TAB ON WEBSITE:
        elif "đóng" in me:
            ai_brain = str(random.choice(voice_vn1))
            os.system("taskkill /im chrome.exe /f")

        # HEAL-CARE:
        elif "sức khỏe" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_HEALTH_CARE_VN)
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            try:
                me = ai_hear_1.recognize_google(audio, language="vi-VN")
                Global.user_text(self, me)
            except:
                me = "Có gì đó không đúng ở đây. Ngài nên thử lại!"
                Global.machine_text(self, me)

            if "nước" in me:
                ai_brain = str(water2)
            elif "ăn" in me:
                curr_date = datetime.today().strftime('%A')
                if curr_date == "Monday":
                    ai_brain = str(food_monday_vn)
                elif curr_date == "Tuesday":
                    ai_brain = str(food_tuesday_vn)
                elif curr_date == "Wednesday":
                    ai_brain = str(food_wednesday_vn)
                elif curr_date == "Thursday":
                    ai_brain = str(food_thursday_vn)
                elif curr_date == "Friday":
                    ai_brain = str(food_friday_vn)
                elif curr_date == "Saturday":
                    ai_brain = str(food_saturday_vn)
                elif curr_date == "Sunday":
                    ai_brain = str(food_sunday_vn)

            elif "cân nặng" in me:
                print("Xin ngài hãy nhập cân nặng và chiều cao!")
                weight = float(input("Cân nặng(kg):  "))
                height = float(input("Chiều Cao(meter): "))

                print("Roxy: Đang tính toán...!")

                bmi = weight / (height ** 2)

                if bmi <= 18.5:
                    ai_brain = "Chỉ số BMI của ngài là " + str(round(bmi, 2)) + ". Ngài đang suy dinh dưỡng đấy! " + \
                               str(wei1_vn)

                elif 18.5 < bmi <= 24.9:
                    ai_brain = "Chỉ số BMI của ngài là " + str(round(bmi, 2)) + ". " + str(wei2_vn)

                elif 25 < bmi <= 34.9:
                    ai_brain = "Chỉ số BMI của ngài là " + str(round(bmi, 2)) + ". Ngài hơi thừa cân đấy! " + \
                               str(wei3_vn) + str(random.choice(activity2))

                elif bmi > 35:
                    ai_brain = "Chỉ số BMI của ngài là " + str(round(bmi, 2)) + ". Ngài bị béo phì rồi nên giảm cân " \
                                                                                "thôi! " + str(wei3_vn) + \
                               str(random.choice(activity2))

            else:
                ai_brain = "Ngài nên theo chỉ dẫn của thực đơn này để giữ cho sức khỏe được khỏe mạnh!"

        # ALARM CLOCK:
        elif "báo thức" in me:
            def validate_time(awake_time):
                if len(awake_time) != 11:
                    err = "Định dạng thời gian không hợp lệ! Vui lòng thử lại..."
                    Global.machine_text(self, err)
                else:
                    if int(awake_time[0:2]) > 12:
                        err1 = "Định dạng GIỜ không hợp lệ! Vui lòng thử lại..."
                        Global.machine_text(self, err1)
                    elif int(awake_time[3:5]) > 59:
                        err2 = "Định dạng PHÚT không hợp lệ! Vui lòng thử lại..."
                        Global.machine_text(self, err2)
                    elif int(awake_time[6:8]) > 59:
                        err3 = "Định dạng GIÂY không hợp lệ! Vui lòng thử lại..."
                        Global.machine_text(self, err3)
                    else:
                        return "ok"

            while True:
                awake_time = input("Nhập thời gian ở định dạng 'HH:MM:SS AM/PM': ")

                validate = validate_time(awake_time.lower())
                if validate != "ok":
                    print(validate)
                else:
                    Global.user_text(self, awake_time)

                    ai_brain3 = "Được rồi, tôi sẽ đánh thức ngài vào lúc " + awake_time

                    Global.machine_text(self, ai_brain3)
                    tts = gTTS(ai_brain3, lang="vi")
                    tts.save("hi.mp3")
                    playsound("hi.mp3")
                    os.remove("hi.mp3")
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
                                ai_brain = "Tới giờ làm việc rồi thưa ngài!"
                                break

        # SEARCHING INFORMATION:
        elif "tìm kiếm" in me or "thông tin" in me:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_INFORMATION_VN)
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            try:
                info = ai_hear_1.recognize_google(audio)
                Global.user_text(self, info)
            except:
                info = "Hình như có gì đó không đúng!"
                Global.machine_text(self, info)

            wikipedia.set_lang("vi")
            ai_brain = wikipedia.summary(info, sentences=8)

        # SAY THANKS YOU:
        elif "cảm ơn" in me or "Cảm ơn" in me:
            ai_brain = str(random.choice(thanks_vn))

        # QUIT:
        elif "tạm biệt" in me or "Tạm biệt" in me:
            ai_brain = str(random.choice(end_vn))

            Global.machine_text(self, ai_brain)
            tts = gTTS(ai_brain, tld="com.vn", lang="vi")
            tts.save("hi.mp3")
            playsound("hi.mp3")
            os.remove("hi.mp3")
            break

        # ANOTHER KEYS:
        else:
            if "thế nào" in me:
                ai_brain = "Tôi khỏe, ngài cần tôi làm gì nào?"
            elif "Cảm ơn" or "cảm ơn" in me:
                ai_brain = str(random.choice(thanks_vn))
            else:
                ai_brain = str(random.choice(unknown_vn))

        Global.machine_text(self, ai_brain)
        tts = gTTS(ai_brain, lang="vi")
        tts.save("hi.mp3")
        playsound("hi.mp3")
        os.remove("hi.mp3")  # delete the current audio file when starting a new loop While
