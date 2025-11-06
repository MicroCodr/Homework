# beg_goblin.py
import random
from entity import Entity

class BegGoblin(Entity):
    def __init__(self):
        hp = random.randint(20, 30)
        super().__init__("Goblin", hp)

    def melee_attack(self, enemy):
        damage = random.randint(3, 6)
        enemy.take_damage(damage)
        return f"{self.name} claws {enemy.name} for {damage} damage!"
