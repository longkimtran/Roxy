import pyttsx3

ai_brain ="Hello Long"
ai_mouth = pyttsx3.init()
voices = ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice', voices[1].id)
ai_mouth.say(ai_brain)
ai_mouth.runAndWait()
