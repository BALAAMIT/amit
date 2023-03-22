import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
from requests import get
import pywhatkit as kit
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('volume')
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0) 
engine.setProperty('voice', voices[1].id)
 
def speak(audio):
    '''speak funcation ka use karke computere  voices use krte hai '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''wishme function ka use time to time wishing ke liye'''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Mornig")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Avtar 0.1 . please tell Me how can I help you")

def takeCommand():
    ''' it take microphone userer and returns string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said {query} \n")
    except Exception as e:
        # print(e)

        speak("say that agian please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        #logic for  executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results =wikipedia.summary(query,sentences = 1)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif"open Notepad" in query:
            codepath1= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            os.startfile(codepath1)

        elif "open command Chrome"in query:
            codepath2 = "start Cmd"
            os.startfile(codepath2)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open facebook"in query:
            webbrowser.open("facebook.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif"the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is : {strTime} ")

        elif"open vs"in query:
            vsco = "C:\\Program Files\\Wilcom\\EmbroideryStudio_e4.2\\BIN\\DESLOADR.EXE"
            os.startfile(vsco) 

        elif"open google" in query:
            speak("sir what should i serch on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open camra" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcom",img)
                k = cv2.waitKey(50)
                if k ==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music = ""
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
            
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")
        
        elif "send massage" in query:
            kit.sendwhatmsg("")
            
