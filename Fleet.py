from Weapon import Weapon
from Robot import Robot


import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        counter = 0
        num_robots = 3 #input("How many robots should report to the fleet?")
        print("Robot Architect begins factory constructrion!")
        while counter<num_robots:
            if counter == 0:
                self.robot_list.append(Robot("Robot Titan",Weapon("Super-Laser Cannon",75)))
                print(self.robot_list[counter].name + " has been built!")
                counter += 1
            else:
                self.robot_list.append(Robot("Robot New-Build"+counter,Weapon("Shrapnel Launcher",40))) 
                print(self.robot_list[counter].name + " has been built!")   
                counter += 1
                