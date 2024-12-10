#Lab test
#Folasayo Owolabi (C23354821)
#03/12/24

import random

####################### CLASESS #######################################

class GameParticipant(object):
    """Class for game particpant"""

    def __init__(self, name="", game_history=[]):
        self.name = name
        self.game_history = game_history

    def __str__(self):
        result = "Player {}".format(self.name)
        return result


class Player(GameParticipant):
    """Class for player"""

    def __init__(self, name="", game_history=[], balance=0, bet="", betamount= 0):
        GameParticipant.__init__(self, name="", game_history=[])
        self.bet = bet
        self.balance = balance
        self.betamount = betamount


    def __str__(self):
        result = GameParticipant.__str__(self)
        result = result + "\n{}'s game history: {}".format(self.name, self.game_history)

    def placebet(self):
        """"To place a bet and update the balance"""
        self.betamount = int(input("\nHow much would you like to bet?: "))

        #update the balance with their bet
        self.update_balance(self.betamount)
        print("\nYour balance is now {}".format(self.balance))

        #get the player's bet of cho or han
        self.bet = input("\n\nChoose cho or han: ").upper()

        return self.bet

    def update_balance(self, amount):
        """To update participant balance after a bet """
        self.balance = self.balance + amount

        return self.balance

    def postgame_balance(self, outcome):
        """To update the balance after playing the game"""

        #True refers to the player having won
        #Add double their bet to their balance
        if outcome is True:
            self.balance = self.balance + (self.betamount*2)
        #if they lose the balance gets decreased by their bet
        else:
            self.balance = self.balance - self.betamount

        self.update_game_history(outcome)
        return self.balance

    def update_game_history(self, outcome):
        """Update the player's game hisotry based on whether they won or lost the round"""

        if outcome is True:
            self.game_history.append("Win")
        else:
            self.game_history.append("Lose")




class DiceCup(object):
    """Class represnting the dice"""

    def __init__(self, dice1=0, dice2=0):
        #roll both dice
        self.dice1 = dice1
        self.dice2 = dice2

    def rollDice(self):
        """Rolls the dice and determines odd or even"""
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

        win = " "

        #get sum
        sum = self.dice2 + self.dice1

        #determine han or cho
        if sum%2 == 0:
            win = "CHO"
        else:
            win = "HAN"

        return win

###############################################################



def menu():
    """Main menu for the game loop"""
    choice = 10

    playername = input("\n\nWhat is your name?: ")
    player = Player(playername)


    while choice != 0:
        choice = int(input("\nEnter 1 to play\nEnter 2 to see Game History\nEnter 0 to end"))

        if choice == 1:

            #get player to place their bet
            cho_or_han = player.placebet()

            #create the dice
            dice = DiceCup()

            #roll the dice and determine han or cho
            outcome = dice.rollDice()

            #check if they got it right
            if cho_or_han == outcome:
                newbalance = player.postgame_balance(True)

                print("\n\nYou win! Your balance is now {}".format(newbalance))

            else:

                newbalance = player.postgame_balance(False)

                print("\n\nYou lose... Your balance is now {}".format(newbalance))

        elif choice == 2:
            print("\n\nGAME HISTORY:\n {}".format(player.game_history))

        else:
            #if choice isn't 1,2 or 0
            if choice != 0:
                print("\nINVALID CHOICE")




menu()
