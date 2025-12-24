class Hand:
    def __init__(self):
        self._cardinhand = []

    def add_card(self, card):
        self._cardinhand.append(card)

    def total(self):
        totalval = sum(card._value for card in self._cardinhand)
        acecount = sum(1 for card in self._cardinhand if card._rank == 'A')
        while totalval > 21 and acecount > 0:
            totalval -= 10
            acecount -= 1
        return totalval


# checkers

    def is_bj(self):
        return self.total() == 21 and len(self._cardinhand) == 2

    def is_bust(self):
        return self.total() > 21


# str


    def __str__(self):
        return ', '.join(str(card) for card in self._cardinhand)
