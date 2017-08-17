from card import Card

from random import shuffle
class Deck(object):
    def __init__(self):
        suits = ("C", "D", "H", "S")
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        #{"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8 , "9":9 , "10": 10, "J": 10, "Q": 10, "K": 10}
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))
                                       
    def shuffle(self):
        shuffle(self.cards)
                
    def draw(self):
        return self.cards.pop()
    
    def show(self):
        for card in self.cards:
            print card