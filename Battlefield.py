import Herd,Fleet

class Battlefield:
    def __init__(self):
        print("Battlefield sequence initiating..")
        self.display_welcome()
        self.herd = Herd()
        self.fleet = Fleet()


    def display_welcome(self):
        print("________________________________________________________________________________\n\t"
        + "Welcome to the 3D combat simulator where your fighting dreams become reality!")

    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        pass

    def robo_turn(self,robot):
        pass

    def show_dino_opponent_options(self):
        pass

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

    def check_forces(self):
        if len(self.fleet.robot_list)==0 or len(self.herd.dinosaur_list)==0:
            self.display_winners()