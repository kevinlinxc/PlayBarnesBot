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

To run my bot straight out of the gate, open the project in Pycharm, install missing dependencies (red underlines), right click and run itssimple.py, and then type y/n in the run window when it prompts you to confirm a tweet. 

If you experience Python version problems, I'm using Python 3.7 and when I open this project on different computers I usually need to make a new interpreter under settings -> Project: PlayBarnesBot -> Proejct Interpreter.

I followed this resource for using tweepy and many stack overflow posts for everything else.
https://realpython.com/twitter-bot-python-tweepy/
