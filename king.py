from colorama import init, Fore, Back, Style
from cannon import Cannon
from base import Base
import os
init()
import global_stuff as gs

base = Base()


class King:

    def movement(self, direction):
        for lol in range(gs.KING_SPEED):
            if gs.KING_HEALTH > 0:
                x = gs.king_pos[0]
                y = gs.king_pos[1]
                if direction == "UP" and gs.building[x - 1][y] == " ":
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + " "
                    gs.building[a][b] = " "

                    gs.king_pos[0] = gs.king_pos[0] - 1
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + "K"
                    gs.building[a][b] = "KING"

                if direction == "DOWN" and gs.building[x + 1][y] == " ":
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + " "
                    gs.building[a][b] = " "

                    gs.king_pos[0] = gs.king_pos[0] + 1
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + "K"
                    gs.building[a][b] = "KING"

                if direction == "RIGHT" and gs.building[x][y + 1] == " ":
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + " "
                    gs.building[a][b] = " "

                    gs.king_pos[1] = gs.king_pos[1] + 1
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + "K"
                    gs.building[a][b] = "KING"

                if direction == "LEFT" and gs.building[x][y - 1] == " ":
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + " "
                    gs.building[a][b] = " "

                    gs.king_pos[1] = gs.king_pos[1] - 1
                    a = gs.king_pos[0]
                    b = gs.king_pos[1]
                    gs.board[a][b] = Fore.WHITE + "K"
                    gs.building[a][b] = "KING"




    def update(self):
            a = gs.king_pos[0]
            b = gs.king_pos[1]
            gs.board[a][b] = Fore.WHITE + "K"
            gs.building[a][b] = "KING"

    def attack(self, ki,last_direction):
        if ki == 1:
            x = gs.king_pos[0]
            y = gs.king_pos[1]
            if gs.building[x - 1][y] != " " and gs.KING_HEALTH>=0:
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                building_targeted = gs.building[x - 1][y]
                if building_targeted == "WIZARD1":
                    gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.wiz1_cord)
                elif building_targeted == "WIZARD2":
                    gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.wiz2_cord)
                elif building_targeted == "WIZARD3":
                    gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.wiz3_cord)
                elif building_targeted == "WIZARD4":
                    gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.wiz4_cord)
                elif building_targeted == "CANNON1":
                    gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - gs.KING_ATTACK
                    if gs.CANNON1_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon1_cord)
                elif building_targeted == "CANNON2":
                    gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - gs.KING_ATTACK
                    if gs.CANNON2_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon2_cord)
                elif building_targeted == "CANNON3":
                    gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - gs.KING_ATTACK
                    if gs.CANNON3_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon3_cord)
                elif building_targeted == "CANNON4":
                    gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - gs.KING_ATTACK
                    if gs.CANNON4_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon4_cord)
                elif building_targeted == "WIZARD1":
                    gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.wiz1_cord)
                elif building_targeted == "WIZARD2":
                    gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.wiz2_cord)
                elif building_targeted == "WIZARD3":
                    gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.wiz3_cord)
                elif building_targeted == "WIZARD4":
                    gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.wiz4_cord)
                elif building_targeted == "TH":
                    gs.TH_HEALTH = gs.TH_HEALTH - gs.KING_ATTACK
                    if gs.TH_HEALTH < 0:
                        gs.buildings_pos.remove(gs.town_hall_cord)
                elif building_targeted == "HUTS1":
                    gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.hut1_cord)
                elif building_targeted == "HUTS2":
                    gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.hut2_cord)
                elif building_targeted == "HUTS3":
                    gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.hut3_cord)
                elif building_targeted == "HUTS4":
                    gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.hut4_cord)
                elif building_targeted == "HUTS5":
                    gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[4] < 0:
                        gs.buildings_pos.remove(gs.hut5_cord)
                elif building_targeted == "WALLS":
                    gs.board[x - 1][y] = " "
                    gs.building[x - 1][y] = " "
            elif gs.building[x + 1][y] != " " and gs.KING_HEALTH>=0:
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                building_targeted = gs.building[x + 1][y]
                if building_targeted == "CANNON1":
                    gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - gs.KING_ATTACK
                    if gs.CANNON1_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon1_cord)
                elif building_targeted == "CANNON2":
                    gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - gs.KING_ATTACK
                    if gs.CANNON2_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon2_cord)
                elif building_targeted == "CANNON3":
                    gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - gs.KING_ATTACK
                    if gs.CANNON3_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon3_cord)
                elif building_targeted == "CANNON4":
                    gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - gs.KING_ATTACK
                    if gs.CANNON4_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon4_cord)
                elif building_targeted == "WIZARD1":
                    gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.wiz1_cord)
                elif building_targeted == "WIZARD2":
                    gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.wiz2_cord)
                elif building_targeted == "WIZARD3":
                    gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.wiz3_cord)
                elif building_targeted == "WIZARD4":
                    gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.wiz4_cord)
                elif building_targeted == "TH":
                    gs.TH_HEALTH = gs.TH_HEALTH - gs.KING_ATTACK
                    if gs.TH_HEALTH < 0:
                        gs.buildings_pos.remove(gs.town_hall_cord)
                elif building_targeted == "HUTS1":
                    gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.hut1_cord)
                elif building_targeted == "HUTS2":
                    gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.hut2_cord)
                elif building_targeted == "HUTS3":
                    gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.hut3_cord)
                elif building_targeted == "HUTS4":
                    gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.hut4_cord)
                elif building_targeted == "HUTS5":
                    gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[4] < 0:
                        gs.buildings_pos.remove(gs.hut5_cord)
                elif building_targeted == "WALLS":
                    gs.board[x + 1][y] = " "
                    gs.building[x + 1][y] = " "
            elif gs.building[x][y + 1] != " " and gs.KING_HEALTH>=0:
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                building_targeted = gs.building[x][y + 1]
                if building_targeted == "CANNON1":
                    gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - gs.KING_ATTACK
                    if gs.CANNON1_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon1_cord)
                elif building_targeted == "CANNON2":
                    gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - gs.KING_ATTACK
                    if gs.CANNON2_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon2_cord)
                elif building_targeted == "CANNON3":
                    gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - gs.KING_ATTACK
                    if gs.CANNON3_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon3_cord)
                elif building_targeted == "CANNON4":
                    gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - gs.KING_ATTACK
                    if gs.CANNON4_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon4_cord)
                elif building_targeted == "WIZARD1":
                    gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.wiz1_cord)
                elif building_targeted == "WIZARD2":
                    gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.wiz2_cord)
                elif building_targeted == "WIZARD3":
                    gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.wiz3_cord)
                elif building_targeted == "WIZARD4":
                    gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.wiz4_cord)
                elif building_targeted == "TH":
                    gs.TH_HEALTH = gs.TH_HEALTH - gs.KING_ATTACK
                    if gs.TH_HEALTH < 0:
                        gs.buildings_pos.remove(gs.town_hall_cord)
                elif building_targeted == "HUTS1":
                    gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.hut1_cord)
                elif building_targeted == "HUTS2":
                    gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.hut2_cord)
                elif building_targeted == "HUTS3":
                    gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.hut3_cord)
                elif building_targeted == "HUTS4":
                    gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.hut4_cord)
                elif building_targeted == "HUTS5":
                    gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[4] < 0:
                        gs.buildings_pos.remove(gs.hut5_cord)
                elif building_targeted == "WALLS":
                    gs.board[x][y + 1] = " "
                    gs.building[x][y + 1] = " "
            elif gs.building[x][y - 1] != " " and gs.KING_HEALTH>=0:
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                building_targeted = gs.building[x][y - 1]
                if building_targeted == "CANNON1":
                    gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - gs.KING_ATTACK
                    if gs.CANNON1_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon1_cord)
                elif building_targeted == "CANNON2":
                    gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - gs.KING_ATTACK
                    if gs.CANNON2_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon2_cord)
                elif building_targeted == "CANNON3":
                    gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - gs.KING_ATTACK
                    if gs.CANNON3_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon3_cord)
                elif building_targeted == "CANNON4":
                    gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - gs.KING_ATTACK
                    if gs.CANNON4_HEALTH < 0:
                        gs.buildings_pos.remove(gs.cannon4_cord)
                elif building_targeted == "WIZARD1":
                    gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.wiz1_cord)
                elif building_targeted == "WIZARD2":
                    gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.wiz2_cord)
                elif building_targeted == "WIZARD3":
                    gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.wiz3_cord)
                elif building_targeted == "WIZARD4":
                    gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK
                    if gs.WIZARD_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.wiz4_cord)
                elif building_targeted == "TH":
                    gs.TH_HEALTH = gs.TH_HEALTH - gs.KING_ATTACK
                    if gs.TH_HEALTH < 0:
                        gs.buildings_pos.remove(gs.town_hall_cord)
                elif building_targeted == "HUTS1":
                    gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[0] < 0:
                        gs.buildings_pos.remove(gs.hut1_cord)
                elif building_targeted == "HUTS2":
                    gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[1] < 0:
                        gs.buildings_pos.remove(gs.hut2_cord)
                elif building_targeted == "HUTS3":
                    gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[2] < 0:
                        gs.buildings_pos.remove(gs.hut3_cord)
                elif building_targeted == "HUTS4":
                    gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[3] < 0:
                        gs.buildings_pos.remove(gs.hut4_cord)
                elif building_targeted == "HUTS5":
                    gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - gs.KING_ATTACK
                    if gs.HUT_HEALTH[4] < 0:
                        gs.buildings_pos.remove(gs.hut5_cord)
                elif building_targeted == "WALLS":
                    gs.board[x][y - 1] = " "
                    gs.building[x][y - 1] = " "
        
        else:
            # print("king positions: " + str(gs.king_pos))
            direction =[]
            positions=[]
            if last_direction == "w":
                positions = [-8,0] 
            elif last_direction == "s":
                positions = [8,0]
            elif last_direction == "a":
                positions = [0,-8]
            elif last_direction == "d":
                positions = [0,8]
            for i in range(5):
                    for j in range(5):
                        direction.append([positions[0]+i-2,positions[1]+j-2])
            flag = [False for i in range(14)]
            for d in direction:
                x = gs.king_pos[0]
                y = gs.king_pos[1]
                if gs.building[d[0]+gs.king_pos[0]][d[1] + gs.king_pos[1]] != " " and gs.KING_HEALTH>=0:
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    building_targeted = gs.building[d[0]+gs.king_pos[0]][d[1] + gs.king_pos[1]]
                    if building_targeted == "WIZARD1" and flag[0] == False:
                        flag[0] = True
                        gs.WIZARD_HEALTH[0] = gs.WIZARD_HEALTH[0] - gs.KING_ATTACK*0.85
                        if gs.WIZARD_HEALTH[0] < 0:
                            gs.buildings_pos.remove(gs.wiz1_cord)
                    elif building_targeted == "WIZARD2" and flag[1] == False:
                        flag[1] = True
                        gs.WIZARD_HEALTH[1] = gs.WIZARD_HEALTH[1] - gs.KING_ATTACK*0.85
                        if gs.WIZARD_HEALTH[1] < 0:
                            gs.buildings_pos.remove(gs.wiz2_cord)
                    elif building_targeted == "WIZARD3" and flag[2] == False:
                        flag[2] = True
                        gs.WIZARD_HEALTH[2] = gs.WIZARD_HEALTH[2] - gs.KING_ATTACK*0.85
                        if gs.WIZARD_HEALTH[2] < 0:
                            gs.buildings_pos.remove(gs.wiz3_cord)
                    elif building_targeted == "WIZARD4" and flag[3] == False:
                        flag[3] = True
                        gs.WIZARD_HEALTH[3] = gs.WIZARD_HEALTH[3] - gs.KING_ATTACK*0.85
                        if gs.WIZARD_HEALTH[3] < 0:
                            gs.buildings_pos.remove(gs.wiz4_cord)
                    elif building_targeted == "CANNON1" and flag[4] == False:
                        flag[4] = True
                        gs.CANNON1_HEALTH = gs.CANNON1_HEALTH - gs.KING_ATTACK*0.85
                        if gs.CANNON1_HEALTH < 0:
                            gs.buildings_pos.remove(gs.cannon1_cord)
                    elif building_targeted == "CANNON2" and flag[5] == False:
                        flag[5] = True
                        gs.CANNON2_HEALTH = gs.CANNON2_HEALTH - gs.KING_ATTACK*0.85
                        if gs.CANNON2_HEALTH < 0:
                            gs.buildings_pos.remove(gs.cannon2_cord)
                    elif building_targeted == "CANNON3" and flag[6] == False:
                        flag[6] = True
                        gs.CANNON3_HEALTH = gs.CANNON3_HEALTH - gs.KING_ATTACK*0.85
                        if gs.CANNON3_HEALTH < 0:
                            gs.buildings_pos.remove(gs.cannon3_cord)
                    elif building_targeted == "CANNON4" and flag[7] == False:
                        flag[7] = True
                        gs.CANNON4_HEALTH = gs.CANNON4_HEALTH - gs.KING_ATTACK*0.85
                        if gs.CANNON4_HEALTH < 0:
                            gs.buildings_pos.remove(gs.cannon4_cord)
                    elif building_targeted == "TH" and flag[8] == False:
                        flag[8] = True
                        gs.TH_HEALTH = gs.TH_HEALTH - gs.KING_ATTACK*0.85
                        if gs.TH_HEALTH < 0:
                            gs.buildings_pos.remove(gs.town_hall_cord)
                    elif building_targeted == "HUTS1" and flag[9] == False:
                        flag[9] = True
                        gs.HUT_HEALTH[0] = gs.HUT_HEALTH[0] - gs.KING_ATTACK*0.85
                        if gs.HUT_HEALTH[0] < 0:
                            gs.buildings_pos.remove(gs.hut1_cord)
                    elif building_targeted == "HUTS2" and flag[10] == False:
                        flag[10] = True
                        gs.HUT_HEALTH[1] = gs.HUT_HEALTH[1] - gs.KING_ATTACK*0.85
                        if gs.HUT_HEALTH[1] < 0:
                            gs.buildings_pos.remove(gs.hut2_cord)
                    elif building_targeted == "HUTS3" and flag[11] == False:
                        flag[11] = True
                        gs.HUT_HEALTH[2] = gs.HUT_HEALTH[2] - gs.KING_ATTACK*0.85
                        if gs.HUT_HEALTH[2] < 0:
                            gs.buildings_pos.remove(gs.hut3_cord)
                    elif building_targeted == "HUTS4" and flag[12] == False:
                        flag[12] = True
                        gs.HUT_HEALTH[3] = gs.HUT_HEALTH[3] - gs.KING_ATTACK*0.85
                        if gs.HUT_HEALTH[3] < 0:
                            gs.buildings_pos.remove(gs.hut4_cord)
                    elif building_targeted == "HUTS5" and flag[13] == False:
                        flag[13] = True
                        gs.HUT_HEALTH[4] = gs.HUT_HEALTH[4] - gs.KING_ATTACK*0.85
                        if gs.HUT_HEALTH[4] < 0:
                            gs.buildings_pos.remove(gs.hut5_cord)
                    elif building_targeted == "WALLS":
                        gs.board[d[0]+gs.king_pos[0]][d[1] + gs.king_pos[1]] = " "
                        gs.building[d[0]+gs.king_pos[0]][d[1] + gs.king_pos[1]] = " "