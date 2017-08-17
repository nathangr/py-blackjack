from deck import Deck
from dealer import Dealer
from player import Player
from blackjackhand import BlackjackHand

class GameController(object):
    def __init__ (self):
        self.player_bet = 0
    
    def prep_player(self):
        self.player = Player()
    
    def prep_dealer(self):
        dealer_deck = Deck()
        dealer_deck.shuffle()
        self.dealer = Dealer(dealer_deck)
        
    def ask_player_bet(self):
        self.player_bet = self.player.ask_bet()
        
    def hand_to_player(self):
        self.player.take_card(self.dealer.deal_card())
        self.player.take_card(self.dealer.deal_card())
        self.player.show_hand()
        
    def hand_to_dealer(self):
        self.dealer.take_card(self.dealer.deal_card())
        self.dealer.take_card(self.dealer.deal_card())
        self.dealer.show_hand()
        
    def check_initial_hands(self):
        if self.dealer.hand.is_blackjack() == True and self.player.hand.is_blackjack() == True:
            print "Both you and the dealer have a Blackjack!"
            self.dealer.show_hand(False)
            return "tie"
        if self.dealer.hand.is_blackjack() == True and self.player.hand.is_blackjack() == False:
            print "Dealer has Blackjack!"
            self.dealer.show_hand(False)
            return "dealer"
        if self.dealer.hand.is_blackjack() == False and self.player.hand.is_blackjack() == True:
            print "Player has Blackjack!"
            return "player"

        return "game goes on"
            
    def process_blackjack(self, outcome):
        if outcome == "player":
            self.player.bankroll += self.player_bet * 1.5
        elif outcome == 'dealer':
            self.player.bankroll -= self.player_bet
            
    def do_player_turn(self):
        while self.player.hand.is_busted() == False:
            answer = self.player.play_turn()
            if answer == "h":
                self.player.take_card(self.dealer.deal_card())
                self.player.show_hand()
                continue
            elif answer == "s":
                return
            
    def check_player(self):
        if self.player.hand.is_busted() == True:
            print "You busted"
            return "player_busted"
        else:
            return "player_ok"
        
    def do_dealer_turn(self):
        self.dealer.play_turn()
        
    def check_dealer(self):
        if self.dealer.hand.is_busted() == True:
            print "Dealer busted"
            return "dealer_busted"
        else:
            return "dealer_ok"
        
    def find_winner(self):
        if self.player.hand.get_total() == self.dealer.hand.get_total():
            print "Both you and the dealer have " + str(self.dealer.hand.get_total())
            return "tie"
        if self.player.hand.get_total() > self.dealer.hand.get_total():
            print "You win with " + str(self.player.hand.get_total())
            return "player"
        else:
            print "Dealer wins with " + str(self.dealer.hand.get_total())
            return "dealer"
    
    def handle_game_outcome(self, outcome):
        if outcome == "player":
            self.player.bankroll += self.player_bet
        if outcome == "dealer":
            self.player.bankroll -= self.player_bet
        print "You now have: $" + str(self.player.bankroll)
        
    def collect_used_cards(self):
        self.player.empty_hand()
        self.dealer.empty_hand()
        
    def ask_play(self):
        while True:
            answer = raw_input("Do you want to play Blackjack?[y/n] ")
            if answer not in "yn":
                continue
            else:
                return answer == "y"