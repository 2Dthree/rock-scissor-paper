import random

ROCK = 1
SCISSOR = 2
PAPER = 3
typeToText = {ROCK: "Rock", SCISSOR: "Scissor", PAPER: "Paper"}
INITIALDECKSIZE = 15
INITIALHANDSIZE = 8

round = 0

def ordinal(_int):
    if _int == 1:
        return "st"
    elif _int == 2:
        return "nd"
    elif _int == 3:
        return "rd"
    else:
        return "th"

def isLeftWon(card1, card2):
    if card1 == ROCK and card2 == SCISSOR:
        return 1
    elif card1 == SCISSOR and card2 == PAPER:
        return 1
    elif card1 == PAPER and card2 == ROCK:
        return 1
    else:
        return 0

def isRightWon(card1, card2):
    if card1 == ROCK and card2 == PAPER:
        return 1
    elif card1 == SCISSOR and card2 == ROCK:
        return 1
    elif card1 == PAPER and card2 == SCISSOR:
        return 1
    else:
        return 0

class Card:
    def __init__(self, _type):
        self.type = _type
    def __str__(self):
        return "<" + typeToText[self.type] + ">"

class Deck:
    def __init__(self):
        self.cards = []
        self.generate()
    def generate(self):
        for i in range(INITIALDECKSIZE):
            self.cards.append(Card(i%3 + 1))
    def size(self):
        return len(self.cards)

class Player:
    def __init__(self, _name):
        self.name = _name
        self.hand = []
        self.point = 0
    def hasAllType(self):
        hasRock = False
        hasScissor = False
        hasPaper = False
        for card in self.hand:
            if card.type == ROCK:
                hasRock = True
            elif card.type == SCISSOR:
                hasScissor = True
            elif card.type == PAPER:
                hasPaper = True
        if hasRock and hasScissor and hasPaper:
            return True
        else:
            return False
    def getCardsFromDeck(self, _deck):
        self.hand = random.sample(_deck.cards, INITIALHANDSIZE)
    def __str__(self):
        result = "[" + self.name + "]"
        for card in self.hand:
            result += " " + str(card)
        return result

print("--------Rock Scissors Paper--------")
d1 = Deck()
d2 = Deck()
p1 = Player("Player 1")
p1.getCardsFromDeck(d1)
p2 = Player("Player 2")
p2.getCardsFromDeck(d2)

while p1.hasAllType() and p2.hasAllType():
    round += 1
    print(str(round) + ordinal(round) + "\tpoint: " + str(p1.point) + " " + str(p1))
    print("\tpoint: " + str(p2.point) + " " + str(p2))
    print("Which type of card do you select? ROCK: 1, SCISSOR: 2, PAPER: 3")
    p1_input = int(input(p1.name + "'s turn: "))
    p2_input = int(input(p2.name + "'s turn: "))
    for card in p1.hand:
        if card.type == p1_input:
            p1.hand.remove(card)
            break
    for card in p2.hand:
        if card.type == p2_input:
            p2.hand.remove(card)
            break
    p1.point += isLeftWon(p1_input, p2_input)
    p2.point += isRightWon(p1_input, p2_input)
    if isLeftWon(p1_input, p2_input) == 1:
        print(p1.name + " won.")
    elif isRightWon(p1_input, p2_input) == 1:
        print(p2.name + " won.")
    else:
        print("Draw.")

print("-------------Game end-------------")
print(p1.name + "'s point is " + str(p1.point) + ", and " + p2.name + "'s point is " + str(p2.point) + ".")
if p1.point > p2.point:
    print(p1.name + " has won.")
elif p1.point == p2.point:
    print("Draw.")
elif p1.point < p2.point:
    print(p2.name + " has won.")