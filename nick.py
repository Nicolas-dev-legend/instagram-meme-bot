from instabot import Bot
import requests


r =requests.get("https://meme-api.herokuapp.com/gimme")


import json

response = json.loads(r.text)
url = response['url']
title = response['title']


r = requests.get(url)


open("nick.jpg","wb").write(r.content)
import time
bot = Bot()
time.sleep(5)


bot.login(username = "nickthelegend2",
          password = "Nicolas1234@",
          )
bot.upload_photo("nick.jpg",caption = title)
print(url)
print(title)
