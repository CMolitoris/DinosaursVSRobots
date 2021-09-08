class Robot:
    def __init__(self,name,weapon):
        self.name = name
        self.health = 200
        self.weapon = weapon

    def attack(self,dinosaur):
        damage = self.weapon.attack_power
        dinosaur.health -= damage
        print(self.name + " inflicted " + str(damage) + " to " + dinosaur.name + " (" + str(dinosaur.health) + " remaining)")    