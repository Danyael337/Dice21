import json
import os
from player import Player

class Game:
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Player("Dealer")
        self.highscore_file = "highscore.txt"
        self.highscore = self.load_highscore()

    # --- Highscore-hantering ---
    def load_highscore(self):
        """Läser in highscore från fil om den finns, annars skapas en ny."""
        if os.path.exists(self.highscore_file):
            with open(self.highscore_file, "r") as f:
                return json.load(f)
        return {"Spelare": 0, "Dealer": 0, "Oavgjort": 0}

    def save_highscore(self):
        """Sparar highscore till fil."""
        with open(self.highscore_file, "w") as f:
            json.dump(self.highscore, f)

    # --- Spelrundor ---
    def player_turn(self):
        """Hantera spelarens tur."""
        while True:
            print(f"\nDin poäng: {self.player.score}")
            val = input("Vill du (r)ulla eller (s)tanna? ").lower()

            if val not in ["r", "s"]:
                print("⚠️ Ogiltigt val. Skriv 'r' för rulla eller 's' för stanna.")
                continue

            if val == "r":
                roll = self.player.roll_dice()
                print(f"🎲 Du rullade {roll}. Totalt: {self.player.score}")
                if self.player.score > 21:
                    print("💥 Du fick över 21! Du förlorar.")
                    return "Dealer"
            else:
                print(f"🧍 Du stannar på {self.player.score}.")
                return None  # Gå vidare till dealern

    def dealer_turn(self):
        """Dealern slår tills den når minst 17."""
        print("\n--- Dealerns tur ---")
        while self.dealer.score < 17:
            roll = self.dealer.roll_dice()
            print(f"💻 Dealern rullade {roll}. Totalt: {self.dealer.score}")
            if self.dealer.score > 21:
                print("💥 Dealern fick över 21! Du vinner.")
                return "Spelare"
        print(f"🧍 Dealern stannar på {self.dealer.score}.")
        return None

    def check_winner(self):
        """Avgör vinnaren enligt reglerna."""
        if self.player.score > 21:
            return "Dealer"
        elif self.dealer.score > 21:
            return "Spelare"
        elif self.player.score > self.dealer.score:
            return "Spelare"
        elif self.dealer.score > self.player.score:
            return "Dealer"
        else:
            return "Oavgjort"

    def reset_scores(self):
        """Återställ poäng inför ny runda."""
        self.player.reset()
        self.dealer.reset()

    # --- Huvudspel ---
    def play(self):
        print("🎲 Välkommen till Tärningsspelet 21! 🎲")

        while True:
            self.reset_scores()

            result = self.player_turn()
            if result is None:  # Bara om spelaren inte förlorat direkt
                dealer_result = self.dealer_turn()
                result = dealer_result if dealer_result else self.check_winner()

            # Uppdatera och spara highscore
            self.highscore[result] += 1
            self.save_highscore()

            # Visa resultat
            print("\n--- Resultat ---")
            print(f"Spelare: {self.player.score}")
            print(f"Dealer: {self.dealer.score}")
            print(f"🏆 Vinnare: {result}")
            print(f"📈 Ställning: {self.highscore}")

            again = input("\nVill du spela igen? (j/n): ").lower()
            if again != "j":
                print("\nTack för att du spelade! 👋")
                break
