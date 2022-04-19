from numpy import Inf
import global_stuff as gs    
from colorama import init, Fore, Back, Style
class Troops:
    def __init__(self):
        self.attack = gs.BARBARIAN_ATTACK
        self.health = gs.BARBARIAN_HEALTH
        self.x = 0
        self.y = 0
    def spawn(self,inp):
        gs.BARBARIAN_COUNT = gs.BARBARIAN_COUNT + 1
        if gs.BARBARIAN_COUNT >= 10:
            pass
        elif inp == "i":
            gs.troops_pos.append([11,45])
            gs.board[11][45] = Fore.WHITE + "B"
            self.x = 11
            self.y = 45
        elif inp == "o":
            gs.troops_pos.append([30,21])
            gs.board[30][21] = Fore.WHITE + "B"
            self.x = 30
            self.y = 21
        elif inp == "p":
            gs.troops_pos.append([41,49])
            gs.board[40][50] = Fore.WHITE + "B"
            self.x = 41
            self.y = 49
    def move(self):
        for trp in gs.troops_pos:
            distance = 5001
            for buildng in gs.buildings_pos:
                for p in buildng:
                    if abs(trp[0] - p[0]) + abs(trp[1] - p[1]) < distance:
                        distance = abs(trp[0] - p[0]) + abs(trp[1] - p[1])
                        destination = p
            if distance != 5001:
                if distance == 1 or (distance == 2 and trp[0] != destination[0] and trp[1] != destination[1]):
                    ## attack
                    # destination = [x,y]
                    if gs.building[destination[0]][destination[1]] == "CANNON1":
                        gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - self.attack
                    elif gs.building[destination[0]][destination[1]] == "CANNON2":
                        gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - self.attack
                    elif gs.building[destination[0]][destination[1]] == "CANNON3":
                        gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - self.attack
                    elif gs.building[destination[0]][destination[1]] == "CANNON4":
                        gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - self.attack
                    elif gs.building[destination[0]][destination[1]] == "HUTS1":
                        gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "HUTS2":
                        gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "HUTS3":
                        gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "HUTS4":
                        gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "HUTS5":
                        gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "TH":
                        gs.TH_HEALTH = gs.TH_HEALTH - self.attack

                    elif gs.building[destination[0]][destination[1]] == "WIZARD1":
                        gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "WIZARD2":
                        gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "WIZARD3":
                        gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - self.attack
                    elif gs.building[destination[0]][destination[1]] == "WIZARD4":
                        gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - self.attack
                    
                else:
                    gs.board[trp[0]][trp[1]] = Fore.WHITE + " "
                    if trp[0] < destination[0]:
                        trp[0] = trp[0] + 1
                    elif trp[0] > destination[0]:
                        trp[0] = trp[0] - 1
                    if trp[1] < destination[1]:
                        trp[1] = trp[1] + 1
                    elif trp[1] > destination[1]:
                        trp[1] = trp[1] - 1
                    gs.board[trp[0]][trp[1]] = Fore.WHITE + "B"
                    self.x = trp[0]
                    self.y = trp[1]