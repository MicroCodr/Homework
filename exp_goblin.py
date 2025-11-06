import random
from entity import Entity

class ExpGoblin(Entity):
    def __init__(self):
        hp = random.randint(40, 55)
        super().__init__("Horrible Goblin", hp)  # scarier name!

    def melee_attack(self, enemy):
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return f"{self.name} viciously slashes {enemy.name} for {damage} damage!"
