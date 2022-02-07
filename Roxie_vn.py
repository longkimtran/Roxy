# Some libraries use in AV
import os
import random
import subprocess
import webbrowser
from datetime import date, datetime

import speech_recognition as sr
import wikipedia
from gtts import gTTS
from playsound import playsound
import requests
from bs4 import BeautifulSoup

from Data_Roxie import hello_vn, google_vn, end_vn, unknown_vn, \
    thanks_vn, voice_vn1, web_data
from Data_Roxie3 import water2, food_friday_vn, food_monday_vn, food_saturday_vn, \
    food_sunday_vn, food_thursday_vn, food_tuesday_vn, food_wednesday_vn


def Roxie2():
    ai_hear = sr.Recognizer()
    ai_hear_1 = sr.Recognizer()

    while True:
        with sr.Microphone() as mic:  # Use micro in system
            print("Roxie: Tôi đang nghe !")
            audio = ai_hear.listen(mic, timeout=6, phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

        print("Roxie:....")
        try:
            me = ai_hear.recognize_google(audio, language="vi-VN")
        except:
            me = "Tôi không hiểu !"
        print("You: " + me)

        if "Xin chào" in me:
            ai_brain = str(random.choice(hello_vn))

        elif "ngày" in me:
            today = date.today()  # use current date real life
            ai_brain = today.strftime("%d/%m/%Y")

        elif "giờ" in me:
            now = datetime.now()
            ai_brain = now.strftime("%H:%M:%S")

        elif "Google" in me:
            ai_brain = str(random.choice(google_vn))
            webbrowser.open('https://www.google.com.vn/')

        elif "giải trí" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: Ngài muốn giải trí như thế nào? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear_1.recognize_google(audio, language="vi-VN")
            except:
                me = "Có gì đó không đúng ở đây. Ngài nên thử lại!"
            print("You: " + me)

            if "trình duyệt" in me:
                ai_brain = str(random.choice(voice_vn1))
                webbrowser.open(random.choice(web_data))

            elif "âm nhạc" in me:
                subprocess.call(r'C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe')

            elif "game" or "trò chơi" in me:
                with sr.Microphone() as mic:  # Use micro in system
                    print("Roxie: Ngài muốn chơi game gì?")
                    audio = ai_hear_1.listen(mic, timeout=6,
                                             phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

                print("Roxie:....")
                try:
                    me = ai_hear_1.recognize_google(audio, language="vi-VN")
                except:
                    me = "Có gì đó không đúng!"

                print("You: " + me)
                if "steam" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    subprocess.call(r'C:\Program Files (x86)\Steam\steam.exe')

                elif "garena" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    subprocess.call(r'C:\Program Files (x86)\Garena\Garena\Garena.exe')

                elif "valorant" in me:
                    ai_brain = str(random.choice(voice_vn1))
                    subprocess.call(r'D:\playgame\Riot Games\Riot Client\RiotClientServices.exe')
                else:
                    ai_brain = "Trò chơi của ngài không tồn tại hoặc chưa cài đặt!"
            else:
                ai_brain = "Không có ứng dụng giải trí ngài cần. Xin hãy thử lại!"

        elif "đóng" in me:
            ai_brain = str(random.choice(voice_vn1))
            os.system("taskkill /im chrome.exe /f")

        elif "sức khỏe" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: Hôm nay ngài cần gì về sức khỏe ? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                me = ai_hear_1.recognize_google(audio, language="vi-VN")
            except:
                me = "Có gì đó không đúng ở đây. Ngài nên thử lại!"
            print("You: " + me)

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
            else:
                ai_brain = "Ngài nên theo chỉ dẫn của thực đơn này để giữ cho sức khỏe được khỏe mạnh!"

        elif "tìm kiếm" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: Bạn muốn tìm gì à? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                info = ai_hear_1.recognize_google(audio)
            except:
                info = "Hình như có gì đó không đúng!"
            print("You: " + info)

            wikipedia.set_lang("vi")
            ai_brain = wikipedia.summary(info, sentences=8)

        elif "nhiệt độ" in me:
            with sr.Microphone() as mic:  # Use micro in system
                print("Roxie: Ngài muốn nhiệt độ ở đâu? ")
                audio = ai_hear_1.listen(mic, timeout=6,
                                         phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            print("Roxie:....")
            try:
                temp = ai_hear_1.recognize_google(audio, language="vi-VN")
            except:
                temp = "Có j đó không đúng!"
            print("You: " + temp)

            url = f"https://www.google.com/search?q={temp}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            # Web Scraping Values on Google Search Results Page
            temp2 = data.find("div", class_='BNeawe').text
            ai_brain = temp + " là " + temp2

        elif "tạm biệt" in me:
            ai_brain = str(random.choice(end_vn))

            print("Roxie: " + ai_brain)
            tts = gTTS(ai_brain, tld="com.vn", lang="vi")
            tts.save("hi.mp3")
            playsound("hi.mp3")
            break
        else:
            if "thế nào" in me:
                ai_brain = "Tôi khỏe, ngài cần tôi làm gì nào?"
            elif "Cảm ơn" or "cảm ơn" in me:
                ai_brain = str(random.choice(thanks_vn))
            else:
                ai_brain = str(random.choice(unknown_vn))
        print("Roxie: " + ai_brain)
        tts = gTTS(ai_brain, lang="vi")
        tts.save("hi.mp3")
        playsound("hi.mp3")
        os.remove("hi.mp3")  # delete the current audio file when starting a new loop While
