class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def is_ace(self):
        return self.rank == 'A'
    
    def __str__(self):
        return self.suit + ":" + self.rank