class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._value = self.compute_value()

    def compute_value(self):
        if self._rank in ["J", "K", "Q"]:
            return 10
        elif self._rank == "A":
            return 11
        else:
            return int(self._rank)


# str

    def __str__(self):
        return f"▸{self._rank} of {self._suit}◂"
