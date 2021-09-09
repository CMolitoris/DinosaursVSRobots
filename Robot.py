import random
from Weapon import Weapon
from ColorPrint import ColorPrint

class Robot:
    def __init__(self,name):
        self.color = ColorPrint()
        self.name = name
        self.health = 150
        self.power = 20
        self.weapon = self.choose_weapon()

    def attack(self,dinosaur,dinosaur_list):
        if self.power>=10:
            damage = self.weapon.attack_power
            dinosaur.health -= damage
            self.color.print_blue(self.name + " inflicted " + str(damage) + " damage to " + dinosaur.name + "! (" + str(dinosaur.health) + " health remaining)\n")  
            if dinosaur.health<=0:
                self.color.print_blue(dinosaur.name + " has been slain!\n")  
                index = dinosaur_list.index(dinosaur)
                dinosaur_list.pop(index)
            self.power -= 10
        else:
            self.color.print_blue(self.name + " does not have enough power to attack\n")        

    def choose_weapon(self):
        weapon_options = {1:Weapon("Incinerator",35),2:Weapon("Plasma disintegrator",40),3:Weapon("Savo-Launcher",45)}  
        weapon = weapon_options.get(random.randint(1,3))
        self.color.print_blue(weapon.name + " has been selected")    
        return weapon        