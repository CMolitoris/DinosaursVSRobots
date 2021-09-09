from math import fabs
from Herd import Herd
from Fleet import Fleet
import time
import random
from ColorPrint import ColorPrint

class Battlefield:
    def __init__(self):
        self.color = ColorPrint()
        self.display_welcome()
        self.herd = Herd()
        self.fleet = Fleet()
        self.commence_battle()
        
    def display_welcome(self):
        self.color.print_green("________________________________________________________________________________\n"
        + "  Welcome to the 3D combat simulator where your fighting dreams become reality")
        self.color.print_green("\nBattlefield sequence initiating..")
        time.sleep(2)

    def battle(self):
        done = False
        turn_counter = 0
        while not done:
            dice_roll = self.dice_roll()
            if dice_roll>3:
                self.dino_first()        
            else:
                self.robo_first()            
            done = self.check_forces()
            turn_counter += 1
            if done==False:
                self.color.print_bold("End of turn: " + str(turn_counter) + "\n")
            if turn_counter%2==0:
                self.refresh()                     

    def robo_first(self):
        for robo in self.fleet.robot_list:
            dice_roll = self.dice_roll()
            if dice_roll<5:
                self.robo_turn(robo)
            time.sleep(1)    
        for dino in self.herd.dinosaur_list:
            dice_roll = self.dice_roll()
            if dice_roll>2:
                self.dino_turn(dino)
            time.sleep(1)

    def dino_first(self):
        for dino in self.herd.dinosaur_list:
            dice_roll = self.dice_roll()
            if dice_roll>2:
                self.dino_turn(dino) 
            time.sleep(1)               
        for robo in self.fleet.robot_list:
            dice_roll = self.dice_roll()
            if dice_roll<5:
                self.robo_turn(robo)   
            time.sleep(1)              

    def dino_turn(self,dinosaur):
        attack = self.show_dino_opponent_options(dinosaur)
        if len(self.fleet.robot_list)==1:
            robot = self.fleet.robot_list[0]
        else:
            robot = self.fleet.robot_list[random.randint(0,len(self.fleet.robot_list)-1)]
        dinosaur.attack(robot,attack,self.fleet.robot_list)

    def robo_turn(self,robot):
        if len(self.herd.dinosaur_list)==1:
            dinosaur = self.herd.dinosaur_list[0]
        else:
            dinosaur = self.herd.dinosaur_list[random.randint(0,len(self.herd.dinosaur_list)-1)]
        robot.attack(dinosaur,self.herd.dinosaur_list)

    def show_dino_opponent_options(self,dinosaur):
        attack_list = dinosaur.get_attacks_keys()
        #-- User input can be implemented here --#
        return attack_list[random.randint(0,2)]

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        if len(self.fleet.robot_list)==0:
            self.color.print_bold("The dinosaurs have emerged victorious!\n")
            for dino in self.herd.dinosaur_list:
                self.color.print_red(dino.name + " has survived the battle!")
                
        else:
            self.color.print_bold("The robots have won the battle!\n")
            for robo in self.fleet.robot_list:
                self.color.print_blue(robo.name + " has survived the battle!")
        return True        

    def check_forces(self):
        if len(self.fleet.robot_list)==0 or len(self.herd.dinosaur_list)==0:
            return self.display_winners()    
        return False    

    def dice_roll(self):
        return random.randint(1,6)        

    def commence_battle(self):
        self.battle()

    def refresh(self):
        for dino in self.herd.dinosaur_list:
            dino.stamina = 20
        for robo in self.fleet.robot_list:
            robo.power = 20    