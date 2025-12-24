import time
from player import Player
from dealer import Dealer
from deck import Deck
from hand import Hand


class BlackjackGame:
    def __init__(self):
        self._players = []
        self._allplayers = []
        self._dealer = Dealer()
        self._deck = Deck()
        self._round_no = 0

    def start(self):
        print("₍ᐢ.ˬ.⑅ᐢ₎: Welcome to the Twenty-One table! The cards are whispering...")
        time.sleep(1)
        self.setup_players()
        continue_game = True
        while continue_game == True and self._players != []:
            self._round_no += 1
            time.sleep(2)
            print("\n" + "="*45)
            print(f"🃏 ROUND {self._round_no} BEGINS")
            print("="*45)
            print("\n(The deck is being shuffled. Dealer smirks mysteriously...)")
            time.sleep(2.5)
            self._deck.shuffle()
            self.place_bets()
            self.initial_deal()
            time.sleep(2)
            self.run_player_turns()
            time.sleep(2)
            self.run_dealer_turn()
            time.sleep(2)
            self.resolve_round()
            time.sleep(2)
            self.eliminate_broke_players()
            time.sleep(2)
            continue_game = self.ask_continue()
        time.sleep(2)
        print("\n\n»»-——————————– ٠ ✤ ٠ —–——————————-««")
        print("   Game Over! Final Achievements")
        print("»»-——————————– ٠ ✤ ٠ —–——————————-««")
        for player in self._players:
            time.sleep(2)
            print(
                f"★ {player._name}: {player.achievement_title()} (₱{player._balance} left)")
        for player in self._allplayers:
            time.sleep(2)
            print(
                f"★ {player._name}: {player.achievement_title()} (₱{player._balance} left)")
        print("\n\n₍ᐢ._.ᐢ₎   ₍ᐢ. ̞.ᐢ₎   ₍ᐢ.ˬ.⑅ᐢ₎   (꜆˶ᵔᵕᵔ˶)꜆  ◝(⑅•ᴗ•⑅)◜")
        print("✿ Thanks for playing ... the dealer tips his hat ✿")
        time.sleep(7.5)
        print(
            "\n\n\n\n\n\nThis game was programmed by Mark Jomer Valderama SN: 202505511 of EEE 111 THRU")
        time.sleep(2)
        print("=====================>>> PROGRAM DONE <<<========================")

    def setup_players(self):
        starting_bal = 100
        print("\n̶̶̶̶ ̶«̶ ̶̶̶ ̶ ̶ ̶̶̶ ̶«̶  Player Setup ̶ »̶ ̶̶̶ ̶ ̶ ̶̶̶ ̶»̶ ̶̶̶ ̶ ̶ ")
        while True:
            try:
                print("₍ᐢ.ˬ.⑅ᐢ₎: How many will join the game?")
                num_players = int(input("✎ Enter the number of players: "))
                if num_players < 1:
                    raise ValueError
                break
            except ValueError:
                print("₍ꐦᐢ.ˬ.⑅ᐢ₎: Please enter a valid input!")
        for i in range(1, num_players + 1):
            while True:
                time.sleep(1)
                print(f"\n₍ᐢ.ˬ.⑅ᐢ₎: What's your name Player {i}?")
                name = input(f"✎ Enter name for Player {i}: ").strip()
                if name:
                    if name.lower() == 'admin':
                        print(
                            "\n₍ᐢ.ˬ.⑅ᐢ₎: Welcome back, admin! You lost all the access rights on 12/02/25 20:23:31.22")
                    break
                else:
                    print(
                        "₍ꐦᐢ.ˬ.⑅ᐢ₎: Oh my God! Please! The player name cannot be empty. Please enter a valid name.")
            self._players.append(Player(name, starting_bal))
            time.sleep(1)
            print(
                f"₍ᐢ.ˬ.⑅ᐢ₎: Added Player {i} ({name}) with ₱{starting_bal} starting balance")

        time.sleep(1)
        print("₍ᐢ.ˬ.⑅ᐢ₎: Processing...")
        time.sleep(3)
        print(f"₍ᐢ.ˬ.⑅ᐢ₎: {len(self._players)} player/s are ready to play!")

    def place_bets(self):
        for nplayer in self._players:
            while True:
                try:
                    time.sleep(2)
                    print(
                        f"\n₍ᐢ.ˬ.⑅ᐢ₎: {nplayer._name}, enter your bet. Your current balance is ₱{nplayer._balance}.")
                    bet = int(input(
                        f"✎ Enter Bet (B:₱{nplayer._balance}): "))
                    if bet == nplayer._balance:
                        time.sleep(1)
                        print(
                            "\n(ꀬ⏖ꀬ∴): (Are we actually G to go all in this early in the night?)")
                    if nplayer.place_bet(bet):
                        break
                    else:
                        if bet == 0:
                            time.sleep(1)
                            print(
                                f"\n₍ꐦᐢ.ˬ.⑅ᐢ₎: {nplayer._name}, you are totally trying to go ALL-OUT right now TT. Please bet the minimum amount to play.")
                        else:
                            time.sleep(1)
                            print(
                                f"\n₍ꐦᐢ.ˬ.⑅ᐢ₎: {nplayer._name}, you can’t bet that much! Keep your feet on the ground.")
                        continue
                except ValueError:
                    time.sleep(1)
                    print("\n₍ᐢ._.ᐢ₎: Please bet a numerical value.")

    def initial_deal(self):
        self._dealer._hand = Hand()
        for nplayer in self._players:
            nplayer._hand = Hand()
            time.sleep(1)
            print(f"\n✻ (A card was given to {nplayer._name})")
            nplayer.hit(self._deck.deal())
            time.sleep(1)
            print(f"\n✻ (A card was given to {nplayer._name})")
            nplayer.hit(self._deck.deal())
        time.sleep(1)
        print(f"\n✻ (A card was given to the dealer)")
        self._dealer._hand.add_card(self._deck.deal())
        time.sleep(1)
        print(f"\n✻ (A card was given to the dealer)")
        self._dealer._hand.add_card(self._deck.deal())
        time.sleep(1)
        print(
            f"\n\n₍ᐢ.ˬ.⑅ᐢ₎(Dealer): My first revealed card is {self._dealer._hand._cardinhand[0]}!")

    def run_player_turns(self):
        for nplayer in self._players:
            print(f"\n\n₍ᐢ.ˬ.⑅ᐢ₎: It's {nplayer._name}'s turn")
            time.sleep(1)
            print(
                f"✻ {nplayer._name}'s hand | {nplayer._hand} | (Total: {nplayer._hand.total()}/21)\n")
            hitcount = 0
            while not nplayer._hand.is_bust() and not ((nplayer._hand.is_bj()) or (nplayer._hand.total() == 21)):
                time.sleep(2)
                print(
                    f"₍ᐢ.ˬ.⑅ᐢ₎: Choose wisely, {nplayer._name}.")
                choice = input(
                    f"✎  1(Hit)|2(Stand): ").upper()
                if choice == '1':
                    hitcount += 1
                    print(f"\n✻ ({nplayer._name} dares to hit)")
                    nplayer.hit(self._deck.deal())
                    time.sleep(2)
                    print(
                        f"\n(꜆˶ᵔᵕᵔ˶)꜆: I got a {nplayer._hand._cardinhand[1 + hitcount]}.")
                    print(
                        f"✻ {nplayer._name}'s hand: {nplayer._hand} (Total: {nplayer._hand.total()}/21)\n")
                elif choice == '2':
                    print(
                        f"\n₍ᐢ.ˬ.⑅ᐢ₎: HAHAHAHA! {nplayer._name} cowardly stands away from courage.")
                    break
                else:
                    print(
                        "\n₍ꐦᐢ.ˬ.⑅ᐢ₎: Take a (H)int or please (S)tand outside. Play properly.\n")

    def run_dealer_turn(self):
        print("\n\n(꜆˶ᵔᵕᵔ˶)꜆: It's bunny dealer's turn now")
        time.sleep(2)
        print(
            f"\n₍ᐢ.ˬ.⑅ᐢ₎: Okay! FYI!! My second card was {self._dealer._hand._cardinhand[1]}")
        print(
            f"✻ Dealer's hand | {self._dealer._hand} | (Total: {self._dealer._hand.total()}/21)")
        time.sleep(2)
        self._dealer.play_turn(self._deck)
        time.sleep(1)
        print(
            f"✻ Dealer's final hand | {self._dealer._hand} | (Total: {self._dealer._hand.total()}/21)\n")

    def resolve_round(self):
        print("\n✻ (Calculating Results...)")
        time.sleep(2)
        dealer_total = self._dealer._hand.total()
        for nplayer in self._players:
            print("")
            player_total = nplayer._hand.total()
            if player_total == 7 or player_total == 14:
                print(
                    f"₍ᐢ.ˬ.⑅ᐢ₎: {nplayer.name} got {player_total}. Lucky number! Maybe the lottery is winking at you.")

            player_total = nplayer._hand.total()
            if nplayer._hand.is_bj():
                winnings = nplayer._betinround * 2.5
                nplayer._balance += int(winnings)
                nplayer.record_result("win")
                print(
                    f"₍ꐦᐢ.ˬ.⑅ᐢ₎: {nplayer._name} hits Blackjack! (The dealer groans dramatically)")
                time.sleep(1)
                print(
                    f"✻ ({nplayer._name} wins ₱{winnings - nplayer._betinround})")
            elif nplayer._hand.is_bust():
                nplayer.record_result("lose")
                print(
                    f"₍ᐢ.ˬ.⑅ᐢ₎: {nplayer._name} busts! (The dealer chuckles quietly)")
                time.sleep(1)
                print(f"✻ ({nplayer._name} loses ₱{nplayer._betinround})")
            elif self._dealer._hand.is_bust():
                winnings = nplayer._betinround * 2
                nplayer._balance += int(winnings)
                nplayer.record_result("win")
                print(
                    f"(๑>ᴗ<๑): Bunny dealer busts! HAHAHAHAH")
                time.sleep(1)
                print(
                    f"✻ ({nplayer._name} laughs triumphantly and pockets ₱{nplayer._betinround})")
            elif player_total > dealer_total:
                winnings = nplayer._betinround * 2
                nplayer._balance += int(winnings)
                nplayer.record_result("win")
                print("₍ꐦᐢ.ˬ.⑅ᐢ₎: That's absurd!")
                time.sleep(1)
                print(
                    f"✻ ({nplayer._name} laughs triumphantly! {nplayer._name} wins {nplayer._betinround})")
            elif player_total < dealer_total:
                nplayer.record_result("lose")
                print(
                    f"(ꐦ𝅒_𝅒): I...lost... (The dealer gives a smug grin)")
                print(f"✻ ({nplayer._name} loses ₱{nplayer._betinround})")
            else:
                nplayer._balance += nplayer._betinround
                print(
                    f"₍ᐢ.ˬ.⑅ᐢ₎: it seems like {nplayer._name} pushes (The dealer shrugs nonchalantly)")
            if nplayer._balance == 0:
                print(
                    f"✻ ({nplayer._name} is eliminated for zero balance)")

    def eliminate_broke_players(self):
        self._allplayers = [
            player for player in self._players if player._balance <= 0]
        self._players = [
            player for player in self._players if player._balance > 0]
        if self._players:
            print("\n" + "="*45)
            print(f"          Remaining players ({len(self._players)})")
            print("="*45)
            for player in self._players:
                time.sleep(1)
                print(player)
        else:
            print("₍ᐢ.ˬ.⑅ᐢ₎: Every player has been eliminated. Thank you for the game!")

    def ask_continue(self):
        if self._players != []:
            cont = input(
                "₍ᐢ.ˬ.⑅ᐢ₎: ↻ Do you want to continue playing? (Y/N) | ").upper()
            return cont == "Y"
        return False
