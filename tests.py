import random
from player import Player
from game import Game

# --- TESTER FÖR VÄL GODKÄNT ---

def test_roll_dice():
    """Testar att tärningsslaget alltid ger ett värde mellan 1 och 6."""
    p = Player("Test")
    for _ in range(100):
        roll = p.roll_dice()
        assert 1 <= roll <= 6
    print("✅ test_roll_dice OK")

def test_dealer_rule():
    """Testar att dealern stannar vid minst 17 poäng."""
    g = Game()
    g.dealer.score = 16
    random.seed(0)
    g.dealer_turn()
    assert g.dealer.score >= 17
    print("✅ test_dealer_rule OK")

def test_winner_logic():
    """Testar att vinnaren avgörs korrekt i olika scenarier."""
    g = Game()
    g.player.score = 20
    g.dealer.score = 18
    assert g.check_winner() == "Spelare"

    g.player.score = 22
    assert g.check_winner() == "Dealer"

    g.player.score = 19
    g.dealer.score = 19
    assert g.check_winner() == "Oavgjort"
    print("✅ test_winner_logic OK")

if __name__ == "__main__":
    test_roll_dice()
    test_dealer_rule()
    test_winner_logic()
