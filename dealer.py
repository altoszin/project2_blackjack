from hand import Hand
import time


class Dealer:
    def __init__(self):
        self._hand = Hand()

    def play_turn(self, deck):
        card = 2
        while self._hand.total() < 17:
            card += 1
            self._hand.add_card(deck.deal())
            print("\n✻ (A card was given to the dealer)")
            time.sleep(2)
            print(
                f"\n₍ᐢ.ˬ.⑅ᐢ₎: Wow! I got a {self._hand._cardinhand[card - 1]}")
            print(
                f"✻ Dealer's hand | {self._hand} | (Total: {self._hand.total()}/21)")
            time.sleep(2)

    def __str__(self):
        return f"✻ Dealer's hand | {self._hand} | (Total: {self._hand.total()}/21)"
