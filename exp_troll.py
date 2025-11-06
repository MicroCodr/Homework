import random
from entity import Entity

class ExpTroll(Entity):
    def __init__(self):
        hp = random.randint(60, 80)
        super().__init__("Angry Troll", hp)  # scarier name!

    def melee_attack(self, enemy):
        damage = random.randint(10, 15)
        enemy.take_damage(damage)
        return f"{self.name} smashes {enemy.name} for {damage} damage!"
