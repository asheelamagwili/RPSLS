# Author: Asheela Magwili
# File: Element Class
# Purpose: Contains all five elements of the game.

moves = ["Rock","Paper","Scissors","Lizard","Spock"]

class Element:
    # Instance variable 
    def __init__(self,name):
        self._name = name

    def name(self):
        return self._name

    # Instance of the class element
    def compareTo(self):
        raise NotImplementedError("Not yet implemented")

### SUBCLASSES

# Subclass 1: Rock
class Rock(Element):
    def __init__(self,name):
        Element.__init__(self,name)
            
    def compareTo(self,Element):
        # Win
        if Element.name() == "scissors":
            result = ["Rock","Scissors","Rock crushes Scissors","Player 1 won the round."]
            return result

        elif Element.name() == "lizard":
            result = ["Rock","Lizard","Rock crushes Lizard","Player 1 won the round."]
            return result
        
        # Lose
        elif Element.name() == "paper":
            result = ["Rock","Paper","Paper covers Rock","Player 2 won the round."]
            return result

        elif Element.name() == "spock":
            result = ["Rock","Spock","Spock vaporizes Rock","Player 2 won the round."]
            return result

        # Tie
        elif Element.name() == "rock":
            result = ["Rock","Rock","Rock equals Rock","Round was a tie."]
            return result

# Subclass 2: Paper
class Paper(Element):
    def __init__(self,name):
        Element.__init__(self,name)
            
    def compareTo(self,Element):
        # Win
        if Element.name() == "rock":
            result = ["Paper","Rock","Paper covers Rock","Player 1 won the round."]
            return result

        elif Element.name() == "spock":
            result = ["Paper","Spock","Paper disproves Spock","Player 1 won the round."]
            return result

        # Lose
        elif Element.name() == "scissors":
            result = ["Paper","Scissors","Scissors cuts Paper","Player 2 won the round."]
            return result

        elif Element.name() == "lizard":
            result = ["Paper","Lizard","Lizard eats Paper","Player 2 won the round."]
            return result

        # Tie
        elif Element.name() == "paper":
            result = ["Paper","Paper","Paper equals Paper","Round was a tie."]
            return result

# Subclass 3: Scissors
class Scissors(Element):
    def __init__(self,name):
        Element.__init__(self,name)
            
    def compareTo(self,Element):
        # Win
        if Element.name() == "paper":
            result = ["Scissors","Paper","Scissors cuts Paper","Player 1 won the round."]
            return result

        elif Element.name() == "lizard":
            result = ["Scissors","Lizard","Scissors decapitate Lizard","Player 1 won the round."]
            return result

        # Lose
        elif Element.name() == "spock":
            result = ["Scissors","Spock","Spock smashes Scissors","Player 2 won the round."]
            return result

        elif Element.name() == "rock":
            result = ["Scissors","Rock","Rock crushes Scissors","Player 2 won the round."]
            return result

        # Tie
        elif Element.name() == "scissors":
            result = ["Scissors","Scissors","Scissors equals Scissors","Round was a tie."]
            return result

# Subclass 4: Lizard
class Lizard(Element):
    def __init__(self,name):
        Element.__init__(self,name)
            
    def compareTo(self,Element):
        # Win
        if Element.name() == "spock":
            result = ["Lizard","Spock","Lizard poisons Spock","Player 1 won the round."]
            return result

        elif Element.name() == "paper":
            result = ["Lizard","Paper","Lizard eats Paper","Player 1 won the round."]
            return result

        # Lose
        elif Element.name() == "rock":
            result = ["Lizard","Rock","Rock crushes Lizard","Player 2 won the round."]
            return result

        elif Element.name() == "scissors":
            result = ["Lizard","Scissors","Scissors decapitate Lizard","Player 2 won the round."]
            return result

        # Tie
        elif Element.name() == "lizard":
            result = ["Lizard","Lizard","Lizard equals Lizard","Round was a tie."]
            return result

# Subclass 5: Spock
class Spock(Element):
    def __init__(self,name):
        Element.__init__(self,name)

    def compareTo(self,Element):
        # Win
        if Element.name() == "scissors":
            result = ["Spock","Rock","Spock smashes Scissors","Player 1 won the round."]
            return result

        elif Element.name() == "rock":
            result = ["Spock","Rock","Spock vaporizes Rock","Player 1 won the round."]
            return result

        # Lose
        elif Element.name() == "lizard":
            result = ["Spock","Lizard","Lizard poisons Spock","Player 2 won the round."]
            return result

        elif Element.name() == "paper":
            result = ["Spock","Paper","Paper disproves Spock","Player 2 won the round."]
            return result

        # Tie
        elif Element.name() == "spock":
            result = ["Spock","Spock","Spock equals Spock","Round was a tie."]
            return result

# Tests code
'''rock = Rock('rock')
paper = Paper('paper')
print(rock.compareTo(paper))
print(paper.compareTo(rock))
print(rock.compareTo(rock))
print("End of Program")'''
