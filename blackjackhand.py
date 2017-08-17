class BlackjackHand(object):
    values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8 , "9":9 , "10": 10, "J": 10, "Q": 10, "K": 10}
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def get_total(self):
        total = 0
        for card in self.cards:
            total += BlackjackHand.values[card.rank]
        for card in self.cards:
            if card.rank == "A" and total <= 11:
                total += 10
        return total
        
    def is_blackjack(self):
        if self.get_total() == 21 and len(self.cards) == 2:
            return True
        else:
            return False
        
    def is_busted(self):
        if self.get_total() > 21:
            return True
        else:
            return False
        
    def is_dealer_limit(self):
        if self.get_total() > 16:
            return True
        else:
            return False
        
    def show(self, hide_card = False):
        print "---"
        if hide_card == False:
            for card in self.cards:
                print card
        else:
            if len(self.cards) > 0:
                print "#:#"
                for card in self.cards[1:]:
                    print card