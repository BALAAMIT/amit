import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(title = "reak reminder",
                            message = "hello sir please take some break from work",
                            timeout = 10
                            )

   
    
        time.sleep(10)      