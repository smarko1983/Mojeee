import time
from playsound import playsound
from datetime import datetime


alarm_time = "00:18"
while True:
    local_time = datetime.now().strftime('%H:%M')
    if local_time == alarm_time:
        playsound("sound.mp3")
        break
    else:
        print("Wait, patience")
        time.sleep(5)