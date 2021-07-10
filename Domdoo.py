import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

print(voices[0].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning sir")
    elif hour >12 and hour <18 :
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("i am Domdoo 1 point o")

if __name__ == "__main__" :
    wishMe()
