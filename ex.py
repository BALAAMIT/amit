from win10toast import ToastNotifier
import turtle 
import time
tosters = ToastNotifier()
tostitel = "take rest"
massage = "drink whater"
mintes = 3
sec = 3
print("reminder set sus.")
time.sleep(10)
tosters.show_toast(tostitel,massage,duration= 10,threaded=True)
while tosters.notification_active:
    time.sleep(2)
