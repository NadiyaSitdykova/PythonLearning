# -*- coding: utf-8 -*-

"""Rock Paper Scissors game
This game will allow the user to play rock, paper, scissors with the computer.
"""
# SyntaxError: invalid syntax (incorrect order of importing)
from random import randint 

options = ["ROCK", "PAPER", "SCISSORS"]

# SyntaxError: invalid syntax; dictionaries require curly brackets rather than hard brackets on both ends
# Also SemanticError: there should be an equal sign instead of a colon after message; a colon used to annotate variables
message = {"tie": "Yawn it's a tie",
           "won": "Yay you won!",
           "lost": "Aww you lost!"} 

# SyntaxError: invalid syntax (function not properly defined; computer_choice not passed as argument)
def decide_winner(user_choice, computer_choice):
    print "you selected: %s" % user_choice
    # TypeError: %d format: a number is required, not str
    print "computer selected: %s" % computer_choice 

    if user_choice == computer_choice:
        # Semantic error: "lost" should read "tie"; code will run but will not produce the intended results)
        print message["tie"]
    elif user_choice == options[0] and computer_choice == options[2]: 
        print message["won"]
    elif user_choice == options[1] and computer_choice == options[0]:
        print message["won"]
    # Semantic error: 'if' used instead of 'elif' (code will run but will not produce the intended results)
    # IndexError: list index out of range (list indices begin at 0 and not 1)
    elif user_choice == options[2] and computer_choice == options[1]:
        print message["won"]
    else:
        # Semantic error: "tie" should read "lost"; code will run but will not produce the intended results)
        print message["lost"]
      
def play_RPS():
    # raw_input and user_choice are swapped; equality used instead of assignment
    user_choice = raw_input("Enter Rock, Paper, or Scissors")
    # Semantic error: user_choice.upper() needs to be saved in user_choice (code will run but will not produce the intended results)       
    user_choice = user_choice.upper()
    # ValueError: empty range for randrange() (2,1,-1)
    computer_choice = options[randint(0,2)]
    decide_winner(user_choice, computer_choice)
# Semantic error: play_RPS() should not be indented (code will run but will not play the game)
play_RPS()
