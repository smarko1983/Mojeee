# MYP 4 students showed me this website where we were testing our
# click speed. The website is: https://cpstester.com/5-seconds/
# It is basically how many left mouse click can you produce in 5 seconds.
# The score were from 34 to 39
# So I wanted to use a program which could help me achieve better results
# It turns out that there is a excellent pyautogui library

# I experimented for 2 hours
# This is the experiment process, from top to bottom



# import pyautogui
# import time
#
#
#
#
# time.sleep(5)
#
# pyautogui.click()
# time.sleep(0.1)
# for _ in range(90):
#     pyautogui.click()
# 46 clicks is the result


# import pyautogui
# import time
#
# time.sleep(5)
# pyautogui.click()
# time.sleep(0.1)
# [ pyautogui.click() for _ in range(60) ]
# 46 is the result


# using numpy
# import numpy as np  # you first need to pip install it
# import pyautogui
# import time
#
# nums = np.arange(1,80)
# time.sleep(7)
# pyautogui.click()
# time.sleep(0.1)
#
# for _ in nums:
#   pyautogui.click()

# using while True showed the same score, 46



# no loops - the same result - 46
# import pyautogui
# import time
#
#
# time.sleep(7)
# pyautogui.click()
# time.sleep(0.1)
#
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()


# let's try to remove the pyautogui dot call
# the result was the same, 46 clicks
# from pyautogui import click
# import time
#
#
# time.sleep(7)
# click()
# time.sleep(0.1)
#
# while  True:
#   click()



# using a function - I got a slight improvement - result is 47

# from pyautogui import click
# import time
#
# time.sleep(7)
#
#
# def clicker():
#   while  True:
#     click()
#
# time.sleep(0.1)
#
# clicker()

# function - no loops - still 47
from pyautogui import click
# import time
#
# time.sleep(7)
#
#
# def clicker():
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#   click()
#
# time.sleep(0.1)
#
# clicker()




# now I discovered that the click method has a argument clicks, which pycharm did not display
# After this, I got the score of 90 because clicks = 90

# Let's try to experiment a bit more, let's try clicks = 500...
# It worked! I got the score of 500

# Let's get wild...let's try 100 000
# It did not work...
# Wait, it worked...but the website crashed...I got the maximum score:
# You're an Fox!
#
# You Clicked with the speed of 1777.00
#
# 8885 Clicks in 5 Seconds




from pyautogui import click
import time

time.sleep(7)


def clicker():
  click(clicks = 90)  # I changed clicks from 90 to 500, than to 100 000

time.sleep(0.5)
clicker()
