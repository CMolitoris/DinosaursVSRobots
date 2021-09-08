class Dinosaur:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.attack_power = 35

    def attack(self,robot):
        damage = self.attack_power
        robot.health -= damage
        print(self.name + "is attacking! (Loud dinosaur noises!) " + self.name + " has inflicted " + str(damage) + " points of damage (" + str(robot.health) + " remaining)")    