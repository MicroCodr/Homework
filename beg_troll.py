import random
from entity import Entity

class BegTroll(Entity):
    def __init__(self):
        hp = random.randint(30, 45)
        super().__init__("Troll", hp)

    def melee_attack(self, enemy):
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return f"{self.name} clubs {enemy.name} for {damage} damage!"
