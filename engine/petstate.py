from engine.config import LEVEL_2_CUTOFF, LEVEL_3_CUTOFF


class PetState:
    def __init__(self, health: int, defense: int) -> 'PetState':
        self.perm_health = health
        self.perm_defense = defense
        self.sub_level = 1

    def start_new_round(self, round: int):
        self.health = self.perm_health
        self.defense = self.perm_defense

    def get_level(self):
        if self.sub_level == LEVEL_3_CUTOFF:
            return 3
        elif self.sub_level >= LEVEL_2_CUTOFF:
            return 2
        else:
            return 1