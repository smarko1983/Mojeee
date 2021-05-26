import time
from playsound import playsound
from datetime import datetime


# the sound file needs to be in the same directory as the python file
# sometimes, we want to convert it to a wav type of file

alarm_time = "00:18"
while True:
    local_time = datetime.now().strftime('%H:%M')
    if local_time == alarm_time:
        playsound("sound.mp3")
        break
    else:
        print("Wait, patience")
        time.sleep(5)
