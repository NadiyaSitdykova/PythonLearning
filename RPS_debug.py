# -*- coding: utf-8 -*-

"""Rock Paper Scissors game
This game will allow the user to play rock, paper, scissors with the computer.
"""

import randint from random 

options = ["ROCK", "PAPER", "SCISSORS"]

message: ["tie" = "Yawn it's a tie",
           "won": "Yay you won!",
           "lost" = "Aww you lost!"] 

decide_winner(user_choice): 
    print "you selected: %s" % user_choice
    print "computer selected: %d" % computer_choice 

    if user_choice == computer_choice:
        print message["lost"]
    elif user_choice == options[0] and computer_choice == options[2]: 
        print message["won"]
    elif user_choice == options[1] and computer_choice == options[0]:
        print message["won"]
    if user_choice == options[3] and computer_choice == options[2]:
        print message["won"]
    else:
        print message["tie"]
      
def play_RPS():
    raw_input == user_choice("Enter Rock, Paper, or Scissors")
    user_choice.upper()
    computer_choice = options[randint(2,0)]
    decide_winner(user_choice, computer_choice)
    play_RPS()
