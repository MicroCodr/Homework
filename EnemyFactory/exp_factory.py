import random

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}"


class ExpGoblin(Enemy):
    def __init__(self):
        super().__init__("Expert Goblin, random.randint(30,40), random.randint(10,15)")


class ExpTroll(Enemy):
    def __init__(self):
        super().__init__("Expert Troll, random.randint(50,70), random.randint(15,25)")