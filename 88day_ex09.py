import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
mytext =['rahul' ,'rohan','rsmi','rohit','rakesh']
for i in mytext:
    engine.say(f"hi soutout {i}")
engine.runAndWait()
engine.stop()
engine.runAndWait()
    


