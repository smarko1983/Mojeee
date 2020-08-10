import webbrowser
import time
import random
import schedule



def prank():
    count = 0
    while count < 3:
        web_sites = random.choice(["https://www.bilibili.com/video/BV1Gx411n7mC?from=search&seid=3270614089631552711",
                                   "https://memecrunch.com/meme/BYOL6/do-your-homework-meme/image.gif?w=500&c=1", "https://s18670.pcdn.co/wp-content/uploads/willy-wonka-2.jpg"])
        time.sleep(random.randrange(15, 30))
        webbrowser.open(web_sites)
        count += 1

schedule.every().day.at("02:45").do(prank())


