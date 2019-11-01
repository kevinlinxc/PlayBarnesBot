# Description
This bot is a Twitter bot that tweets "Its simple, I play Barnes and I summon ____" as a variation of the joke by Darkk Mane, a video game youtuber.
## Current Blank Fillers:
1. Google Trends Hot Topics from 2006-2018
2. Random quips that I wrote (samples.txt)
3. Cards Against Humanity white cards (cah.txt)

# Recreating my bot

If you want to make something similar, make a config.json file in the src directory and write something like this: 
```
{
  "keys": {
    "api_key": 1,
    "api_key_secret": 2,
    "consumer_key": 3,
    "consumer_key_secret": 67
  }
}
```
Read through the while loop to see what the options are for sources of the blank filler. 

I followed this resource for using tweepy and many stack overflow posts for everything else.
https://realpython.com/twitter-bot-python-tweepy/
