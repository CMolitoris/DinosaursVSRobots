import random
from Weapon import Weapon


class Robot:
    def __init__(self,name,weapon):
        self.name = name
        self.health = 200
        self.power = 20
        self.weapon = self.choose_weapon()

    def attack(self,dinosaur):
        if self.power>=10:
            damage = self.weapon.attack_power
            dinosaur.health -= damage
            print(self.name + " inflicted " + str(damage) + " to " + dinosaur.name + " (" + str(dinosaur.health) + " remaining)")  
            if dinosaur.health<=0:
                print(dinosaur.name + " has been slain!")  
                del dinosaur
            self.power -= 10
        else:
            print(self.name + " does not have enough power to attack")        

    def choose_weapon(self):
        weapon_options = {1:Weapon("Incinerator",35),2:Weapon("Plasma disintegrator",40),3:Weapon("Savo-Launcher",45)}  
        weapon = weapon_options.get(random.randint(1,3))
        print(weapon.name + " has been selected")    
        return weapon        