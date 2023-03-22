from win10toast import ToastNotifier
import pyttsx3
import time
def DrinkWhaterReminder():
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    toast = ToastNotifier()
    toast.show_toast("Hello, World!")
    massage = "Drink  whater  and take rest"
    for i in range(2):
        engine.say(massage)
    engine.runAndWait()
    engine.stop()
    engine.runAndWait()
for i in range(2):

    if __name__ == "__main__":
        DrinkWhaterReminder()
        time.sleep(3600)


