# Author: Asheela Magwili
# File: Player.py
# Purpose: Hold the Player class that consists of StupidBot, RandomBot, IterativeBot, Human, LastPlayBot, and MyBot

from Element import *
import random

# Instances of each element
rock = Rock('rock')
paper = Paper('paper')
scissors = Scissors('scissors')
lizard = Lizard('lizard')
spock = Spock('spock')

moves = [rock,paper,scissors,lizard,spock]

class Player:

    def __init__(self,name):
        self._name = name

    def name(self):
        return self._name

    def play(self):
        raise NotImplementedError("Not yet implemented")

# SUBCLASSES

#  Stupid Bot
class StupidBot(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def play(self):
        return moves[0]

# Random Bot
class RandomBot(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def play(self):
        return random.choice(moves)

# Iterative Bot
class IterativeBot(Player):
    def __init__(self,name):
        Player.__init__(self,name)
        self.calls = 0

    def play(self):
        self.calls = self.calls + 1
        
        if self.calls <= len(moves):
            return moves[self.calls-1]

# Last Play Bot
class LastPlayBot(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def play(self):
        if self.last_move is None:
            return moves[0]
        else:
            if self.last_move == moves[0]:
                return moves[0]

            elif self.last_move == moves[1]:
                return moves[1]

            elif self.last_move == moves[2]:
                return moves[2]

            elif self.last_move == moves[3]:
                return moves[3]

            elif self.last_move == moves[4]:
                return moves[4]

    # Call before calling play (LastPlay) in main
    def setLast(self,last):
        self.last_move = last

# Human Player
class Human(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    def play(self):
        
        validInput = True
        move_int = 0
        while validInput:
            print("(1) : Rock")
            print("(2) : Paper")
            print("(3) : Scissors")
            print("(4) : Lizard")
            print("(5) : Spock")
            move = input("Enter your move: ")
            
            move_int = int(move)
            if move_int < 6 and move_int > -1:
                validInput = False
            else:
                print("Invalid move.  Please try again")

        return moves[move_int-1]
        
# MyBot Player
class MyBot(Player):
    def __init__(self,name):
        Player.__init__(self,name)

    # This is a copy bot that copies what the opponent chooses everytime
    def play(self):
        # If MyBot is Player 1, it will default to playing Spock
        if self.cur_opp is None:
            return moves[4]
        # If MyBot is Player 2, it will then copy what Player 1 chooses
        else:
            if self.cur_opp == moves[0]:
                return moves[0]

            elif self.cur_opp == moves[1]:
                return moves[1]

            elif self.cur_opp == moves[2]:
                return moves[2]

            elif self.cur_opp == moves[3]:
                return moves[3]

            elif self.cur_opp == moves[4]:
                return moves[4]

    # Helper Function: Captures the opponent's move
    # Must be called before the play() function is called
    def setCur(self,current):
        self.cur_opp = current

## SELF-CHECKS

# Self-Check 1: Iterative Bot
'''p1 = StupidBot('StupidBot')
p2 = IterativeBot('IterativeBot')
p1move = p1.play()
p2move = p2.play()
print(p1move.compareTo(p2move))
p2move = p2.play()
print(p1move.compareTo(p2move))
print("End of File")'''

# Self-Check 2: Human Bot
'''p1 = StupidBot('StupidBot')
p2 = Human('Human')
p1move = p1.play()
p2move = p2.play()
print(p1move.compareTo(p2move))
print("End of File")'''

# Self-Check 3: My Bot
'''print("Game 1: ")
p1 = Human('Human')
p2 = MyBot('MyBot')
p1move = p1.play()
p2.setCur(p1move)
p2move = p2.play()
print(p1move.compareTo(p2move))

print("Game 2: ")
p1move = p1.play()
p2.setCur(p1move)
p2move = p2.play()
print(p1move.compareTo(p2move))
print("End of File")'''

# Self-Check 4: Stupid and Random Bot
'''p1 = StupidBot('StupidBot')
p2 = RandomBot('RandomBot')
p1move = p1.play()
p2move = p2.play()
print("name: ",p1.name())
print(p1move.compareTo(p2move))'''

# Self-Check 5: Last Play Bot
'''print("Game 1:")
p1 = LastPlayBot('LastPlayBot')
p2 = RandomBot('RandomBot')
p1.setLast(None)
p1move = p1.play()
p2move = p2.play()
print(p1move.compareTo(p2move))

print("Game 2:")
p1.setLast(p2move)
p1move = p1.play()
p2move = p2.play()
print(p1move.compareTo(p2move))'''
