"""import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()"""
from pyglet import window

"""import wikipedia

info = input("Enter your info: ")

# setting language to hindi
wikipedia.set_lang("en")

# printing the summary
print(wikipedia.summary(info))"""

"""from gtts import gTTS
import os
from playsound import playsound
ai_brain = "chào bạn"

tts = gTTS (text = ai_brain,tld="com.vn" ,lang = "vi" )
tts.save("hi.mp3")
playsound("hi.mp3")"""

"""import random

hello = ["Hello Sir, How are you ?", "Hi Sir", "How about your day, sir?"]
print(random.choice(hello))
"""

"""import python_weather
import asyncio


async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    a = input("Enter your city: ")

    # fetch a weather forecast from a city
    weather = await client.find(a)

    # returns the current day's forecast temperature (int)
    print(a + ": " + str(float(weather.current.temperature) - 32 * 9 / 5) + " °C")

    # close the wrapper once done
    await client.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())"""

"""from datetime import datetime

a = str(input("Input today:"))
b = datetime.today().strftime('%A')

if a == b:
    print("you well!")
else:
    print("you not smart!")"""

"""import subprocess

subprocess.call(r"C:\\Pictures")"""

"""import webbrowser
import random

webbrowser.open(random.choice(['https://www.nimo.tv/', 'https://www.youtube.com/', 'https://www.keybr.com/']))"""

"""import pyglet

# pick an animated gif file you have in the working directory
ag_file = "Personal Voice Assistant.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

# create a window and set it to the image size
win = pyglet.window.Window(width=sprite.width, height=sprite.height, caption="Roxy")


@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()
"""
"""from tkinter import *
from Main_Roxie import AI
win = Tk()
button1 = Button(win, text="Start", command=AI)
button1.pack()
win.mainloop()"""

"""from tkinter import *
from Main_Roxie import AI

root = Tk()
root.title('Roxy')
button_start = Button(root, text="Start", command=AI, width=30, height=10)
button_start.pack()

root.mainloop()"""

"""import speech_recognition as sr
import pyttsx3
import string
import random
#Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 145) #you can replace it to incease or decrease dound speed default(200)
def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()
#now convert audio to text
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....")
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        speak("error...")
        print("Network connection error")
        return "none"
    return text
#for main function
if __name__ == "__main__":
    while True:
        query = takecom().lower()
        if 'create password' in query or 'c' in query :
            if __name__ == "__main__":
                s1 = string.ascii_lowercase
                s2 = string.ascii_uppercase
                s3 = string.digits
                s4 = string.punctuation
                speak('what do you want to keep the length of the password type here')
                plen =int(takecom())  #p
                s=[]
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))
                print("Your password is:")
                print("".join(random.sample(s,plen)))
                speak("".join(random.sample(s,plen)))
        elif query == 'none':
            continue
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'ok byy'
            speak(ex_exit)
            exit()"""

"""print("Please enter your weight and height, sir!")
weight = float(input("Enter your weight(kg):  "))
height = float(input("Enter your height(meter): "))
bmi = 0
print("Roxy: Calculating...!")

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print(str((round(bmi, 2))) +" You underweight, sir! ")

elif 18.5 < bmi <= 24.9:
    print(str((round(bmi, 2))) + " You normal, sir!")

elif 25.1 <= bmi < 34.9:
    print(str((round(bmi, 2))) + " You overweight, sir! ")

elif bmi >= 35.1:
    print(str((round(bmi, 2))) +" You obese, sir! ")

else:
    ai_brain = "Some thing wrong sir. Try again!"""


"""import pyautogui
screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
pyautogui.click() # Click the mouse at its current location.
pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
pyautogui.move(0, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pyautogui.doubleClick() # Double click the mouse at the
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
pyautogui.keyDown('shift')
pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')"""