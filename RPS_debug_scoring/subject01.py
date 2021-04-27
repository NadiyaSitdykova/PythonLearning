"""Rock Paper Scissors game
This game will allow the user to play rock, paper, scissors with the computer.
"""
from random import randint # Error 1

options = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie": "Yawn it's a tie", # Error 2
           "won": "Yay you won!",
           "lost": "Aww you lost!"} # Error 3

def decide_winner(user_choice, computer_choice): # Error 4
    print "you selected: %s" % user_choice
    print "computer selected: %s" % computer_choice # Error 5

    if user_choice == computer_choice:
        print message["tie"] # Error 6
    elif user_choice == options[0] and computer_choice == options[2]: 
        print message["won"]
    elif user_choice == options[1] and computer_choice == options[0]:
        print message["won"]
    elif user_choice == options[2] and computer_choice == options[1]: # Error 7
        print message["won"]
    else:
        print message["lost"] # Error 8
      
def play_RPS():
    user_choice = raw_input("Enter Rock, Paper, or Scissors") # Error 8
    user_choice = user_choice.upper() # Error 10
    computer_choice = options[randint(0,2)] # Error 11
    decide_winner(user_choice, computer_choice)
play_RPS() # Error 12
