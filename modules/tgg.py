#!/usr/bin/env python
"""
tgg.py - The Geek Group Phenny Module
Phenny Copyright 2008, Sean B. Palmer, inamidst.com
This module is copyright 2011, Steven Vaught
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

''' Keep sqlite local to this module for now '''

import sqlite3


def fortune(phenny, input): 
  import subprocess
  
  subp = subprocess.Popen( ['fortune', '-s', 'computers'] , stdout=subprocess.PIPE)
  
  stdo = subp.communicate()[0]
  
  phenny.say( stdo )


fortune.commands = ['quote', 'fortune']
fortune.example = ".quote"
fortune.priority = 'low'




def minecraft(phenny, input):
  #phenny.say( "The minecraft server is currently down." )
  phenny.say( "The 'official' TGG minecraft server address is: gamerxreviews.net **** The server may or may not be down right now.  Try it and let us know." )

minecraft.commands = ['minecraft']
minecraft.example = ".minecraft"
minecraft.priority = 'low'

def tellPlaceholder(phenny, input):
  phenny.say("Sorry, .tell is not yet implemented.  Use BotSteve: tell ")
tellPlaceholder.commands = ['tell']
tellPlaceholder.example = ['Not yet implemented']
tellPlaceholder.priority = 'low'

def liveStream(phenny, input):
  phenny.say("The Geek Group Live Web Stream can be found at: http://www.ustream.tv/channel/the-geek-group-behind-the-scenes-live-feed ")
liveStream.commands = ['stream']
liveStream.example = ['Not yet implemented']
liveStream.priority = 'low'

def coinFlip(phenny, input):
  import random
  coinResult = random.choice(('Heads!', 'Tails!'))
  phenny.say(coinResult)
coinFlip.commands = ['coin']
coinFlip.example = ['.coin']
coinFlip.priority = 'low'

def logFile(phenny, input):
  phenny.say("Channel history can be found at: http://irclog.perlgeek.de/thegeekgroup/today")
logFile.commands = ['history','log']
logFile.example = ['View the history with:  .history']
logFile.priority = 'low'

def rollD20(phenny, input):
  import random
  diceResult = random.choice( range(1,21) )
  phenny.say( str(diceResult) )
rollD20.commands = ['d20']
rollD20.example = ['.d20']
rollD20.priority = 'low'

def join_greeter(phenny, input):
  """
  Greetings depend on new sqlite database.  Schema is simple:

  CREATE TABLE greetings (id INTEGER PRIMARY KEY, nickname, greeting);

  By default, the datebase lives in the bot's root directory tgg-BotSteve/tgg.db

  Will eventually add auto-create and add code
  """

  db_conn = sqlite3.connect("tgg.db")
  db_curr = db_conn.cursor()

  nick = str(input.nick)
  t = (nick,)
  #db_query = "SELECT * FROM greetings WHERE nickname = '%s';" % nick
  db_curr.execute( "SELECT * FROM greetings WHERE nickname = ?;" , t )
  db_result = db_curr.fetchone()

  if (db_result):
    greet = db_result[2]
    phenny.say(greet)

  db_conn.close()
  
join_greeter.event = 'JOIN'
join_greeter.rule = r'(.*)'
join_greeter.priority = 'low'


if __name__ == '__main__': 
   print __doc__.strip()




