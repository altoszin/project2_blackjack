class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._value = self.compute_value()

    def compute_value(self):
        if self._rank in ["J", "K", "Q"]:
            return 10
        elif self._rank == "A":
            return 11  # what do i use as default value, 1 or 11. problem 1. My biggest problem is that I do not know how to play blackjack so default values are not a thing in my dictionary.
        else:
            return int(self._rank)  # forgot to add int


# str

    def __str__(self):
        return f"▸{self._rank} of {self._suit}◂"
