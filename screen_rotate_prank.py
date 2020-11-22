import win32api
import rotatescreen
import time

screen = rotatescreen.get_primary_display()

for i in range(1,32):
    screen.rotate_to((i * 90) % 360 )
    time.sleep(5)
