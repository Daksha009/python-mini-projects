import time
from plyer import notification


while True:
    print("Please sip some water!!")
    notification.notify(
        title="Hydration Reminder",message="It's time to drink some water!")
    time.sleep(3600) # Wait for 5 seconds before the next reminder
