import tweepy
from pytrends.request import TrendReq
from random import seed
from random import randint
import random
import os


#Constants:
NumOptions = 3
cwd = os.getcwd()

#Tweepy authentication
auth = tweepy.OAuthHandler(1, 2)
auth.set_access_token("1", True)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

printString = ""
randomPick = randint(0, NumOptions)
randomPick = 0
found = 1
while found <2:
    pytrends = TrendReq(hl='en-US', tz=360)
    if randomPick == 0:
        year = randint(2006, 2018)
        top_charts_df = pytrends.top_charts(year, hl='en-US', tz=300, geo='GLOBAL')
        print("Chose Trends for year "+year.__str__())
        printString = top_charts_df.sample(1, frac=None, replace=False, weights=None, random_state=None, axis=0)
    elif randomPick == 1:
        lines = open("samples.txt").read().splitlines()
        print("Chose Samples")
        printString = random.choice(lines)
    else:
        lines = open("cah.txt", encoding="utf8").read().splitlines()
        print("Chose CAH")
        printString = random.choice(lines)
    found = 5

print(printString.title)
# related_queries_dict = pytrends.related_queries() related to games
# print(related_queries_dict)

# api.update_status("It's simple, I play Barnes and I summon")
kw_list = ["Games"]
pytrends.build_payload(kw_list, cat=41, timeframe='now 1-d', geo='', gprop='')

#trending_searches_df = pytrends.trending_searches() #trending searches right now
#print(trending_searches_df.head())

#top_charts_df = pytrends.top_charts(2006, hl='en-US', tz=300, geo='GLOBAL')
#print(top_charts_df.head(10)[0])