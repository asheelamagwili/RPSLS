# Author: Asheela Magwili
# File: Main.py
# Purpose: Simulates a gae of Rock, Paper, Scissors, Lizard, and Spock

from Player import *

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!\n")

# Player Menu
print("Please choose two players: ")
print("1 : Human")
print("2 : StupidBot")
print("3 : RandomBot")
print("4 : IterativeBot")
print("5 : LastPlayBot")
print("6 : MyBot")

# Flag: Checks if input is valid
validInput = True
    
while validInput:
    # Asks for player 1 and player 2
    p1String = input("Select player 1: ")
    p2String = input("Select player 2: ")
        
    # Checks if input is a number then converts it to an int
    p1 = int(p1String)
    p2 = int(p2String)
            
    # Checks if the number if between 1-5 then calls the bots
    if (p1 < 6 and p1 > -1) and (p2 < 6 and p2 > -1):
        validInput = False
    
    # If input is not a number
    else:
        print("Invalid choice(s). Please start over.\n")

# Executes after input is checked for validity

# Creates player instances for player 1
# Human Bot
if p1 == 1:
    #print("HumanBot instance")
    player1 = Human('Human')

# Stupid Bot
elif p1 == 2:
    player1 = StupidBot('StupidBot')

# Random Bot
elif p1 == 3:
    player1 = RandomBot('RandomBot')
    
# Iterative Bot 
elif p1 == 4:
    player1 = IterativeBot('IterativeBot')

# Last Play Bot
elif p1 == 5:
    player1 = LastPlayBot('LastPlayBot')

# My Bot
elif p1 == 6:
    player1 = MyBot('MyBot')

## Creates player 2 instances
if p2 == 1:
    #print("HumanBot instance")
    player2 = Human('Human')

# Stupid Bot
elif p2 == 2:
    player2 = StupidBot('StupidBot')

# Random Bot
elif p2 == 3:
    player2 = RandomBot('RandomBot')
            
# Iterative Bot 
elif p2 == 4:
    player2 = IterativeBot('IterativeBot')

# Last Play Bot
elif p2 == 5:
    player2 = LastPlayBot('LastPlayBot')

elif p2 == 6:
    player2 = MyBot('MyBot') 
    
# Print out Bot 1 vs. Bot 2" here:
temp1 = player1.name()
temp2 = player2.name()
p1Name = temp1.strip()
p2Name = temp2.strip()
print(p1Name + " vs. " + p2Name + ". Go!\n")

## Start game rounds

# Tracks the rounds
maxRounds = 5
curRound = 0

# Tracks the score of each player
p1Score = 0
p2Score = 0

while curRound < maxRounds:
    # Increment round count, convert to string, strip leading and trailing whitespace
    curRound = curRound + 1
    temp3 = str(curRound).strip()
    print("Round " + temp3 + ": ")

    # Special cases for LastPlayBot:
    # When Player 1 or Player 2 is LastPlayBot and it is the first round
    if (p1 == 5 or p2 == 5) and curRound == 1:
        if p1 == 5:
            player1.setLast(None)
        if p2 == 5:
            player2.setLast(None)

        p1move = player1.play()
        p2move = player2.play()

    # When Player 1 or Player 2 is LastPlayBot and it is past the first round
    elif (p1 == 5 or p2 == 5) and curRound > 1:
        if p1 == 5:
            player1.setLast(p2move)
        if p2 == 5:
            player2.setLast(p1move)
        p1move = player1.play()
        p2move = player2.play()

    # Special cases for MyBot:
    # When Player 1 is MyBot and it is the first round
    elif p1 == 6 and curRound == 1:
        player1.setCur(None)
        p1move = player1.play()
        p2move = player2.play()

    # When Player 1 or Player 2 is MyBot and it is past the first round
    elif (p1 == 6 or p2 == 6) and curRound > 1:
        if p1 == 6:
            player1.setCur(p2move)
        if p2 == 6:
            player2.setCur(p1move)
        p1move = player1.play()
        p2move = player2.play()

    # For all other bots
    else:
        p1move = player1.play()
        p2move = player2.play()
   
    # Determines winner
    result = p1move.compareTo(p2move)
   
    # Update player scores
    if str(result[3]) == "Player 1 won the round.":
        p1Score = p1Score + 1

    elif str(result[3]) == "Player 2 won the round.":
        p2Score = p2Score + 1

    elif str(result[3]) == "Round was a tie.":
        pass

    # End of round statistics
    print("Player 1 chose " + result[0])
    print("Player 2 chose " + result[1])
    print(result[2])
    print(result[3] + "\n")

## End of game statistics

# Converts player score to string and strips trailing/leading whitespace
p1Score_str = str(p1Score).strip()
p2Score_str = str(p2Score).strip()

print("Final score is " + p1Score_str + " to " + p2Score_str + ".")

if p1Score > p2Score:
    print("Player 1 wins.")
elif p1Score < p2Score:
    print("Player 2 wins.")
else:
    print("Game was a draw.")
