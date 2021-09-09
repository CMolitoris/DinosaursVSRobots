
class Dinosaur:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.attack_power = 35
        self.stamina = 20
        self.attack_set = ("Maul","Thrash","Stomp")

    def attack(self,robot,attack_bonus=0):
        if self.stamina>=10:
            damage = self.attack_power + attack_bonus
            robot.health -= damage
            print(self.name + " is attacking! (Loud dinosaur noises!)" + str(damage) + " points of damage has been inflicted. (" + str(robot.health) + " health remaining)\n")  
            if robot.health<=0:
                print(robot.name + " has been defeated!")
                del robot
            self.stamina -= 10
        else:
            print(self.name + " does not have enough stamina to attack.\n")

    def get_attacks(self):
        return self.attack_set    