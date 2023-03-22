import pywhatkit
import  pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print (f" you said..:{query}\n")
        return "None"
    except:
        print("say that again")
        return "None"
    return query
strTime= int(datetime.now().strftime("%H"))
update = int((datetime.now)+timedelta(minutes=2).strftime("%M"))
def sendMassage():
    '''sendin massage for what app'''
    speak("Who do you wan to massage")
    a = int(input('''person1 - 1
    parson2 - 2 '''))
    if a == 1:
        speak("What the massage")
        massage = str(input("Enter tha massage"))
        pywhatkit.sendwhatmsg("+91 79787 49401",massage,time_hour = strTime,time_min=update)
    elif a==2:
        speak("What the massage")
        massage = str(input("Enter tha massage"))
        pywhatkit.sendwhatmsg("+91 7067622242",massage,time_hour = strTime,time_min=update)
 