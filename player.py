from blackjackhand import BlackjackHand

class Player(object):
    def __init__(self, bankroll = 100):
        self.bankroll = bankroll
        self.hand = BlackjackHand()
    
    def add_win(self, amount):
        self.bankroll += amount
        print "You win " + str(amount) + "$. You now have " + str(self.bankroll) + "$ left."
        
    def sub_loss(self, amount):
        self.bankroll -= amount
        print "You lose " + str(amount) + "$. You now have " + str(self.bankroll) + "$ left."
    
    def take_card(self, card):
        self.hand.add_card(card)
    
    def empty_hand(self):
        self.hand = BlackjackHand()
    
    def show_hand(self, hide_card = False):
        self.hand.show()
    
    def ask_bet(self):
        while True:
            try:
                bet = int(raw_input('What is your bet? '))
            except:
                print "Bet must be a positive amount."
                continue
            finally:
                if bet == self.bankroll:
                    print "Betting the farm!"
                    return bet
                elif bet > self.bankroll:
                    print "You don't have enough money for this bet."
                elif bet < 0:
                    print "Please bet a positive amount."
                else:
                    return bet
    
    def play_turn(self):
        while True:
            answer = raw_input('Do you want to [h]it or [s]tay? ')
            if answer != 's' and answer != 'h':
                continue
            else:
                return answer