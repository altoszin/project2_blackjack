class Hand:
    def __init__(self):
        self._cardinhand = []

    def add_card(self, card):
        self._cardinhand.append(card)

    def total(self):
        totalval = sum(card._value for card in self._cardinhand)
        # forgot how to simplify codes in one liners
        acecount = sum(1 for card in self._cardinhand if card._rank == 'A')
        while totalval > 21 and acecount > 0:
            totalval -= 10  # handles the 1 value when its over
            acecount -= 1
        return totalval


# checkers

    def is_bj(self):
        # forgot the rules of whats a blackjack and payout sh
        return self.total() == 21 and len(self._cardinhand) == 2

    def is_bust(self):
        return self.total() > 21


# str


    def __str__(self):
        return ', '.join(str(card) for card in self._cardinhand)
