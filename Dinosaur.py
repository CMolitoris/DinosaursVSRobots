class Dinosaur:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.attack_power = 35
        self.stamina = 20
        self.attack_set = ["Stomp","Maul","Thrash"]

    def attack(self,robot):
        if self.stamina>=10:
            damage = self.attack_power
            robot.health -= damage
            print(self.name + " is attacking! (Loud dinosaur noises!) " + self.name + " has inflicted " + str(damage) + " points of damage. (" + str(robot.health) + " remaining)")  
            if robot.health<=0:
                print(robot.name + " has been defeated!")
                del robot
            self.stamina -= 10
        else:
            print(self.name + " does not have enough stamina to attack")

    def get_attacks(self):
        return self.attack_set    