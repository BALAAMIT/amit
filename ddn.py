from plyer import notification
from threading import Timer
import time


def reminder():
    notification.notify(title="Reminder", message=message, timeout=20)


while True:
    message = "whater"
    days = 30
    hours = 2
    minutes = 1
    seconds = 10

    total_time = (days * 86400) + (hours * 3600) + minutes * 60 + seconds

    timer = Timer(total_time, reminder)
    timer.start()

    if input("\nDo you want to add more reminders? If so please enter 'yes': ").casefold() == "yes":
        continue

    time.sleep(total_time)
    break