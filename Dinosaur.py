from ColorPrint import ColorPrint

class Dinosaur:
    def __init__(self,name):
        self.color = ColorPrint()
        self.name = name
        self.health = 150
        self.attack_power = 20
        self.stamina = 20
        self.attack_set = {"Maul":15,"Thrash":10,"Stomp":20}

    def attack(self,robot,attack,robot_list):
        attack_bonus = self.attack_set.get(attack)
        if self.stamina>=10:
            damage = self.attack_power + attack_bonus
            robot.health -= damage
            self.color.print_red(self.name + " uses " + attack + "! (Loud dinosaur noises!) " + str(damage) + " points of damage has been inflicted. (" + str(robot.health) + " health remaining)\n")  
            if robot.health<=0:
                self.color.print_red(robot.name + " has been defeated!\n")
                index = robot_list.index(robot)
                robot_list.pop(index)
            self.stamina -= 10
        else:
            self.color.print_red(self.name + " does not have enough stamina to attack.\n")

    def get_attacks_keys(self):
        return list(self.attack_set.keys())