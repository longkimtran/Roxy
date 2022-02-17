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

import pyglet

# pick an animated gif file you have in the working directory
ag_file = "Personal Voice Assistant.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

# create a window and set it to the image size
win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()
