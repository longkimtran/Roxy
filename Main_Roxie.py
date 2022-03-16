# Some libraries use in AV
import datetime
import sys
import warnings

import pyttsx3
import speech_recognition as sr
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

import Global
from Roxie import Roxie1  # get function Roxie1 from Roxie.py
from Roxie_vn import Roxie2  # get function Roxie1 from Roxie_vn.py
from Roxy_Layout import Ui_Roxy

ai_hear = sr.Recognizer()
ai_hear_1 = sr.Recognizer()
ai_mouth = pyttsx3.init()

warnings.filterwarnings("ignore")


class MainWindow:
    ai_brain = ""

    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_Roxy()
        self.uic.setupUi(self.main_win)
        self.uic.Start_Button.clicked.connect(self.Roxy_AI)
        self.uic.Quit_Button.clicked.connect(self.main_win.close)

    def Roxy_AI(self):
        hour = int(datetime.datetime.now().hour)
        if 8 <= hour <= 12:
            ai_brain2 = "Good morning sir. I'm Roxy your virtual assistance. Please choose your language for you, " \
                        "sir! "
        elif 12 < hour < 18:
            ai_brain2 = "Good afternoon sir. I'm Roxy your virtual assistance. Please choose your language for " \
                        "you, " \
                        "sir! "
        else:
            ai_brain2 = "Good evening sir. I'm Roxy your virtual assistance. Please choose your language for you, " \
                        "sir! "

        voice = ai_mouth.getProperty('voices')
        ai_mouth.setProperty('voice', voice[1].id)  # voice AI: 0(Male), 1(Female)
        Global.machine_text(self, ai_brain2)
        ai_mouth.say(ai_brain2)
        ai_mouth.runAndWait()

        while True:
            with sr.Microphone() as mic:  # Use micro in system
                Global.machine_text(self, Global.MACHINE_WAITING_2)
                audio = ai_hear.listen(mic, timeout=6,
                                       phrase_time_limit=3)  # let the computer listen for exactly 3 seconds

            try:
                me = ai_hear.recognize_google(audio)
                Global.user_text(self, me)

            except:
                me = "I cannot recognize your voice."
                Global.machine_text(self, me)

            if "English" in me:
                Roxie1(self)
                break

            if "Vietnamese" in me:
                Roxie2(self)
                break

            ai_brain = "You not choose or something. Try again!"

            voices = ai_mouth.getProperty('voices')
            ai_mouth.setProperty('voice', voices[1].id)  # voice AI: 0(Male), 1(Female)

            Global.machine_text(self, ai_brain)

            ai_mouth.say(ai_brain)
            ai_mouth.runAndWait()

            QtCore.QCoreApplication.processEvents()

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
