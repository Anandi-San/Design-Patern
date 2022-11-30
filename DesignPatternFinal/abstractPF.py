import random
class one:
    def __str__(self):
        return "As"
class two:
    def __str__(self):
        return "2"
class three:
    def __str__(self):
        return "3"
class four:
    def __str__(self):
        return "4"
class five:
    def __str__(self):
        return "5"
class six:
    def __str__(self):
        return "6"
class seven:
    def __str__(self):
        return "7"
class eight:
    def __str__(self):
        return "8"
class nine:
    def __str__(self):
        return "9"
class ten:
    def __str__(self):
        return "10"
class jenderal:
    def __str__(self):
        return "Jenderal"
class queen:
    def __str__(self):
        return "Queen"
class king:
    def __str__(self):
        return "King"

class Deck:
    def __init__(self, deck_factory=None):
        self.card_factory = deck_factory
    def show_card(self):
        card = self.card_factory.get_card()
        print ("Your card is", card.num())
        print ("Its shape", card)
        print ("Its colour is", self.card_factory.get_colour())

number = [one, two, three, four, five, six, seven, eight, nine, ten, jenderal, queen, king]
class Clover:
    def num(self):
        return random.choice(number)()
    def __str__(self):
        return "Clover"
class Spade:
    def num(self):
        return random.choice(number)()
    def __str__(self):
        return "Spade"
class Diamond:
    def num(self):
        return random.choice(number)()
    def __str__(self):
        return "Diamond"
class Heart:
    def num(self):
        return random.choice(number)()
    def __str__(self):
        return "Heart"

class CloverFactory:
    def get_card(self):
        return Clover()
    def get_colour(self):
        return "Black"
class SpadeFactory:
    def get_card(self):
        return Spade()
    def get_colour(self):
        return "Black"
class DiamondFactory:
    def get_card(self):
        return Diamond()
    def get_colour(self):
        return "Red"
class HeartFactory:
    def get_card(self):
        return Heart()
    def get_colour(self):
        return "Red just like my heart"

def get_factory():
    return random.choice([CloverFactory, SpadeFactory, DiamondFactory, HeartFactory])()

# Show card with various factories
pick = Deck()
for i in range(3):
     pick.card_factory = get_factory()
     pick.show_card()
     print("-"*50)