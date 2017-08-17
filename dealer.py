from blackjackhand import BlackjackHand

class Dealer(object):
    def __init__(self, deck):
        self.deck = deck
        self.hand = BlackjackHand()
        
    def deal_card(self):
        card = self.deck.draw()
        return card
    
    def take_card(self, card):
        self.hand.add_card(card)
        
    def empty_hand(self):
        self.hand = BlackjackHand()
        
    def show_hand(self, hide_card = True):
        self.hand.show(hide_card)
        
    def play_turn(self):
        while True:
            if self.hand.is_dealer_limit() == True:
                return
            if self.hand.is_busted() == True:
                print "Dealer busted!"
                return
            
            card = self.deal_card()
            self.take_card(card)
            self.show_hand()