"""Rock Paper Scissors game
This game will allow the user to play rock, paper, scissors with the computer.
"""

from random import randint 

options = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie":"Yawn it's a tie","won": "Yay you won!","lost":"Aww you lost!"}

def decide_winner(user_choice, computer_choice):
# I think at line 14, 15, there should be something quoting user_choice and computer_choice after %
  print "you selected: %s" % user_choice
  print "computer selected: %s" % computer_choice

if user_choice == computer_choice:
  print message["tie"]
elif "user_choice" == options[0] and "computer_choice" == options[2]:
  print message["won"]
elif "user_choice" == options[1] and "computer_choice" == options[0]:
  print message["won"]
elif "user_choice" == options[2] and "computer_choice" == options[1]:
  print message["won"]
else:
  print message["lost"]
 	 
def play_RPS():
	print "Enter Rock, Paper, or Scissors:"
  user_choice() = raw_input
	user_choice.upper()
	computer_choice = options[randint(2,0)]
decide_winner("user_choice", "computer_choice")
play_RPS()
