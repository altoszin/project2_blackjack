import random
from card import Card


class Deck:
    def __init__(self):
        self._deck = self.create_deck()
        self.shuffle()

    def create_deck(self):
        ranks = ['A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'K', 'Q']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        return [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        print("(The deck is ready. Cards flutter dramatically.)")
        random.shuffle(self._deck)

    def deal(self):
        if self._deck == []:
            # deals with empty decks so it reshuffles every round
            print("(The deck is empty! The dealer quickly grabs a new one.)")
            self._deck = self.create_deck()
            self.shuffle()
        return self._deck.pop()
