from secret import my_username
import time
import random
from long_responses import Bohemian_Rhapsody, ethics_rant, pi, activities

time_types = random.choice(["am", "pm"])
random_right_time = random.randint(1, 12)
random_wrong_time = random.randint(61,99)
state = "start"

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "does robot exist" or "write a song" or "recite pi" or "im bored" or "is this the real life" or "name a key signature" or "adventure game" or "find the word" or "explain theoretical physics" or "what time is it?" in user_message:
    return True
  elif f"{user_message}"[0] == {1, 2, 3, 4, 5, 6, 7, 8, 9} :
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""

def start_pi():  
  global state
  state = "ask digits"
  return "how many digits?"
  
def ask_digits(user_message):
  digits = int(user_message)
  return pi[0:digits]

def start(user_message, user_name):
  if user_message == "does robot exist" :
    return f"{ethics_rant}"

  elif user_message == "write a song" :
    return "under construction, please check back later"
  
  elif user_message == "recite pi" :
    return start_pi()
    
  elif user_message == "im bored" :
    return f"Here is a thing you can do to unboredify yourself: {random.choice(activities)}"
  
  elif user_message == "is this the real life" :
    return Bohemian_Rhapsody
  
  elif user_message == "name a key signature" :
    return "under construction, please check back later"
  
  elif user_message == "adventure game" :
    return "under construction, please check back later"
  
  elif user_message == "find the word" :
    return "under construction, please check back later"
  
  elif user_message == "explain theoretical physics" :
    return "under construction, please check back later"
  
  elif user_message == "what time is it" :
    return f"The time is not {random.randint(1, 12)}:{random.randint(61,99)}{random.choice(["am", "pm"])}"


def respond(user_message, user_name):
  global state
  if state == "start":
    return start(user_message, user_name)
  if state == "ask_digits":
    return ask_digits(user_message)
  
