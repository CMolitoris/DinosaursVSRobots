from math import fabs
import Herd,Fleet
import random

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.commence_battle()

    def display_welcome(self):
        print("________________________________________________________________________________\n"
        + "\tWelcome to the 3D combat simulator where your fighting dreams become reality")

    def battle(self):
        done = False
        turn_counter = 0
        while not done:
            dice_roll = self.dice_roll()
            if dice_roll>3:
                for dino in self.herd.dinosaur_list:
                    dice_roll = self.dice_roll()
                    if dice_roll>3:
                        self.dino_turn(dino)            
                for robo in self.fleet.robot_list:
                    dice_roll = self.dice_roll()
                    if dice_roll<4:
                        self.robo_turn(robo)        
            else:
                for robo in self.fleet.robot_list:
                    dice_roll = self.dice_roll()
                    if dice_roll<4:
                        self.robo_turn(robo)
                for dino in self.herd.dinosaur_list:
                    dice_roll = self.dice_roll()
                    if dice_roll>3:
                        self.dino_turn(dino)            
            done = self.check_forces()
            turn_counter += 1
            print("End of turn: ", turn_counter)
            if turn_counter%2==0:
                self.refresh()                     


    def dino_turn(self,dinosaur):
        dinosaur.attack(self.fleet.robot_list[random.randint(0,len(self.fleet.robot_list)-1)])

    def robo_turn(self,robot):
        robot.attack(self.herd.dinosaur_list[random.randint(0,len(self.herd.dinosaur_list)-1)])

    def show_dino_opponent_options(self,dinosaur):
        attack_list = dinosaur.get_attacks()
        #-- User input can be implemented here --#
        return attack_list[random.randint(1,3)]

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        if len(self.fleet.robot_list)==0:
            print("The dinosaurs have emerged victorious!")
            for dino in self.herd.dinosaur_list:
                print(dino.name + " has survived the battle!")
                
        else:
            print("The robots have won the battle!")
            for robo in self.fleet.robot_list:
                print(robo.name + " has survived the battle!")
        return True        

    def check_forces(self):
        if len(self.fleet.robot_list)==0 or len(self.herd.dinosaur_list)==0:
            return self.display_winners()    
        return False    

    def dice_roll(self):
        return random.randint(1,6)        

    def commence_battle(self):
        print("Battlefield sequence initiating..")
        self.display_welcome()
        self.battle()

    def refresh(self):
        for dino in self.herd.dinosaur_list:
            dino.stamina = 20
        for robo in self.fleet.robot_list:
            robo.power = 20    