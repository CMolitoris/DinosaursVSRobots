from Dinosaur import Dinosaur
from ColorPrint import ColorPrint
import time

from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.color = ColorPrint()
        self.dinosaur_list = []
        self.create_herd()

    def create_herd(self):
        counter = 0
        num_dinosaurs = 3 #input("How many dinosaurs should be called to the battle?")
        self.color.print_red("\nDinosaur leader lets out bellowing roar to call for aid!")
        while counter<num_dinosaurs:
            if counter == 0:
                self.dinosaur_list.append(Dinosaur("Dinosaur Behemoth"))
                self.color.print_red(self.dinosaur_list[counter].name + " has arrived!")
                counter += 1
            else:
                self.dinosaur_list.append(Dinosaur("Dinosaur Wayfarer"+ str((counter))))
                self.color.print_red(self.dinosaur_list[counter].name + " has arrived!")    
                counter += 1    
        time.sleep(1)        