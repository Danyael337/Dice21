import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        """Slår tärningen och uppdaterar poängen."""
        roll = random.randint(1, 6)
        self.score += roll
        return roll

    def reset(self):
        """Återställ spelarens poäng."""
        self.score = 0
