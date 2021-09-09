import time
from Weapon import Weapon
from Robot import Robot
from ColorPrint import ColorPrint

from Robot import Robot

class Fleet:
    def __init__(self):
        self.color = ColorPrint()
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        counter = 0
        num_robots = 3 #input("How many robots should report to the fleet?")
        self.color.print_blue("\nRobot Architect begins factory construction!")
        while counter<num_robots:
            if counter == 0:
                self.robot_list.append(Robot("Robot Titan"))
                self.color.print_blue(self.robot_list[counter].name + " has been built!")
                counter += 1
            else:
                self.robot_list.append(Robot("Robot New-Build"+str(counter))) 
                self.color.print_blue(self.robot_list[counter].name + " has been built!")   
                counter += 1
        time.sleep(1)        
        print("\n")    
                