import speech_recognition as sr

ai_hear = sr.Recognizer()
with sr.Microphone() as mic:
    print("Roxie: I'm hearing !")
    audio = ai_hear.listen(mic)

print("Roxie:....")
try:
    me = ai_hear.recognize_google(audio)
except:
    me = "Something wrong here!"
print("You: " + me)


