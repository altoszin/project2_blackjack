from hand import Hand
import time


class Player:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._betinround = 0
        self._hand = Hand()
        self._wins = 0
        self._losses = 0

    def place_bet(self, amount):
        if 0 < amount <= self._balance:
            self._betinround = amount
            self._balance -= amount
            time.sleep(2)
            print(
                f"\n✻ ({self._name} bravely bets ₱{amount})")
            time.sleep(1)
            print("(⑅˘͈ ᵕ ˘͈ ): Let's see how luck plays out!")
            return True
        else:
            return False

    def hit(self, deck):
        self._hand.add_card(deck)

    def stand(self):
        pass

# addons for fun
    def record_result(self, result):
        if result == "win":
            self._wins += 1
        elif result == "lose":
            self._losses += 1
        if self._losses == 3:
            print(
                f"✻ 💧 The next one will be it! Achievement Unlocked: 'Persistent Gambler'")
        if self._wins == 5:
            print(f"✻ 🔥 Youre on a hot streak! Achievement Unlocked: 'Card Shark'")
        if self._wins == 3:
            print(f"✻ 🔥 Youre on a hot streak! Achievement Unlocked: 'Lucky Hand'")

    def achievement_title(self):
        if self._wins >= 5:
            return "Card Shark"
        elif self._wins >= 3:
            return "Lucky Hand"
        elif self._losses >= 3:
            return "Persistent Gambler"
        return "TNV - The New Victim"


# str


    def __str__(self):
        return f"✻ [{self._name}] - [{self.achievement_title()}] | {self._hand} | (Total: {self._hand.total()}/21) | Balance: ₱{int(self._balance)}"
