import random
from entity import Entity


class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, hp = 100)


    def melee_attack(self, enemy):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        damage  = die1 + die2

        enemy.take_damage(damage)

        return f"{self.name} attacks {enemy.name} in melee for {damage} damage.! ({die1} + {die2})"


if __name__ == "__main__":
    hero1 = Hero("Aragorn")
    hero2 = Hero("Legolas")

    print(f"Inital status: {hero1}, {hero2}")

    #melee attack

    print(hero1.melee_attack(hero2))
    print(f"Status after melee: {hero2}")

    print(hero2.ranged_attack(hero1))
    print(f"Status after ranged: {hero1}")
