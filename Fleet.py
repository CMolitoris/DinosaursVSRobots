from Weapon import Weapon
from Robot import Robot


from Robot import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        counter = 0
        num_robots = 3 #input("How many robots should report to the fleet?")
        print("\nRobot Architect begins factory construction!")
        while counter<num_robots:
            if counter == 0:
                self.robot_list.append(Robot("Robot Titan"))
                print(self.robot_list[counter].name + " has been built!")
                counter += 1
            else:
                self.robot_list.append(Robot("Robot New-Build"+str(counter))) 
                print(self.robot_list[counter].name + " has been built!")   
                counter += 1
            print("\n")    
                