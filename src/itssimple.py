import random
from random import randint
import tweepy
import tweepy as tweepy
from pytrends.request import TrendReq
import json

# Constants:
NumOptions = 3

# Open config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Tweepy authentication
auth = tweepy.OAuthHandler(config['keys']['api_key'], config['keys']['api_key_secret'])
auth.set_access_token(config['keys']['consumer_key'], config['keys']['consumer_key_secret'])
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Helper methods
# checks if the word has been used before, returns true if so
def checkHistory(string):
    with open('search.txt') as file:
        if string in file.read():
            print(string + ' has been used already')
            return True
        else:
            print(string + ' hasn\'t been used before')
            return False


# writes the unused word to search.txt aka the history
def addHistory(string):
    with open('search.txt', "a", encoding="utf-8") as file:
        file.write(string)
        file.write("\n")


#set up shit
printString = ""
randomPick = randint(0, NumOptions)
found = 1

#find words until we find a new word
while found < 2:
    #The Google Trends outcome:
    pytrends = TrendReq(hl='en-US', tz=360)
    if randomPick == 0:
        year = randint(2006, 2018)
        top_charts_df = pytrends.top_charts(year, hl='en-US', tz=300, geo='GLOBAL')
        print("Chose Trends for year " + year.__str__())
        randomIndex = randint(0, 9)
        for index, row in top_charts_df.iterrows():
            if index == randomIndex:
                if (checkHistory(row.title)):
                    print("Searching for new word")
                else:
                    addHistory(row.title)
                    printString = row.title
                    found = 5
    #The self-written quips outcome:
    elif randomPick == 1:
        lines = open("samples.txt").read().splitlines()
        print("Chose Samples")
        chosenSamplesString = random.choice(lines)
        if (checkHistory(chosenSamplesString)):
            print("Searching for new word")
        else:
            addHistory(chosenSamplesString)
            printString = chosenSamplesString
            found = 5
    #The Card Against Humanity outcome
    else:
        lines = open("cah.txt", encoding="utf8").read().splitlines()
        print("Chose CAH")
        chosenCAHString = random.choice(lines)
        if (checkHistory(chosenCAHString)):
            print("Searching for new word")
            break
        else:
            addHistory(chosenCAHString)
            printString = chosenCAHString
            found = 5

api.update_status('It\'s simple, I play Barnes and I summon ' + str(printString))

# related_queries_dict = pytrends.related_queries() related to games
# print(related_queries_dict)

# api.update_status("It's simple, I play Barnes and I summon")
# kw_list = ["Games"]
# pytrends.build_payload(kw_list, cat=41, timeframe='now 1-d', geo='', gprop='')

# trending_searches_df = pytrends.trending_searches() #trending searches right now
# print(trending_searches_df.head())

# top_charts_df = pytrends.top_charts(2006, hl='en-US', tz=300, geo='GLOBAL')
# print(top_charts_df.head(10)[0])
