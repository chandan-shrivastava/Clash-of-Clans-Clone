from archer import Archers
from balloon import Balloons
from input import Get, input_to
from colorama import init, Fore, Back, Style
import os
import global_stuff as gs
from base import Base
from king import King
from troops import Troops
from cannon import Cannon
from health import Health
from spell import Spell
from wizard import Wizard
import os.path

init()

Get().hide_cursor()
os.system("clear")
last_direction = "w"
base = Base()
king = King()
cannon = Cannon()
health = Health()
wizard = Wizard()
archers = Archers()
ballons = Balloons()

ki = int(input("Press 1 for King, Press 2 for Queen"))
for i in range(1000):
    if os.path.exists("replays/no" + str(i)):
        continue
    else:
        file1 = open("replays/no" + str(i), "a")
        break
while True:
    if gs.level == 1 and gs.runonce1 == 0:
        gs.runonce1 = 1
        gs.building_alive = 10
        base.townhall("GREEN")
        base.wall()
        base.cannon(1, "GREEN")
        base.cannon(2, "GREEN")
        base.hut(1, "GREEN")
        base.hut(2, "GREEN")
        base.hut(3, "GREEN")
        base.hut(4, "GREEN")
        base.hut(5, "GREEN")
        base.wizard_tower(1, "GREEN")
        base.wizard_tower(2, "GREEN")
        base.spawn_point()
        base.boundary()
        king.update()
        for j in range(4):
            j = j + 50
            for i in range(3):
                i = i + 25
                gs.town_hall_cord.append([i, j])
        gs.cannon1_cord = [[25, 35], [24, 34], [24, 35], [25, 34]]
        gs.cannon2_cord = [[25, 71], [24, 71], [24, 70], [25, 70]]
        gs.hut1_cord = [[15, 71], [14, 71], [14, 70], [15, 70]]
        gs.hut2_cord = [[35, 71], [34, 71], [34, 70], [35, 70]]
        gs.hut3_cord = [[15, 34], [14, 34], [14, 35], [15, 35]]
        gs.hut4_cord = [[15, 55], [14, 55], [14, 54], [15, 54]]
        gs.hut5_cord = [[35, 51], [34, 51], [34, 50], [35, 50]]
        gs.wiz1_cord = [[15, 63], [14, 63], [14, 62], [15, 62]]
        gs.wiz2_cord = [[35, 61], [34, 61], [34, 60], [35, 60]]
        gs.buildings_pos.append(gs.town_hall_cord)
        gs.buildings_pos.append(gs.cannon1_cord)
        gs.buildings_pos.append(gs.cannon2_cord)
        gs.buildings_pos.append(gs.hut1_cord)
        gs.buildings_pos.append(gs.hut2_cord)
        gs.buildings_pos.append(gs.hut3_cord)
        gs.buildings_pos.append(gs.hut4_cord)
        gs.buildings_pos.append(gs.hut5_cord)
        gs.buildings_pos.append(gs.wiz1_cord)
        gs.buildings_pos.append(gs.wiz2_cord)
    elif gs.level == 2 and gs.runonce2 == 0:

        gs.runonce2 = 1
        gs.building_alive = 12
        base.townhall("GREEN")
        base.wall()
        base.cannon(1, "GREEN")
        base.cannon(2, "GREEN")
        base.cannon(3, "GREEN")
        base.hut(1, "GREEN")
        base.hut(2, "GREEN")
        base.hut(3, "GREEN")
        base.hut(4, "GREEN")
        base.hut(5, "GREEN")
        base.wizard_tower(1, "GREEN")
        base.wizard_tower(2, "GREEN")
        base.wizard_tower(3, "GREEN")
        base.spawn_point()
        base.boundary()
        king.update()
        for j in range(4):
            j = j + 50
            for i in range(3):
                i = i + 25
                gs.town_hall_cord.append([i, j])
        gs.cannon1_cord = [[25, 35], [24, 34], [24, 35], [25, 34]]
        gs.cannon2_cord = [[25, 71], [24, 71], [24, 70], [25, 70]]
        gs.cannon3_cord = [[17, 51], [18, 51], [18, 50], [17, 50]]
        gs.hut1_cord = [[15, 71], [14, 71], [14, 70], [15, 70]]
        gs.hut2_cord = [[35, 71], [34, 71], [34, 70], [35, 70]]
        gs.hut3_cord = [[15, 34], [14, 34], [14, 35], [15, 35]]
        gs.hut4_cord = [[15, 55], [14, 55], [14, 54], [15, 54]]
        gs.hut5_cord = [[35, 51], [34, 51], [34, 50], [35, 50]]
        gs.wiz1_cord = [[15, 63], [14, 63], [14, 62], [15, 62]]
        gs.wiz2_cord = [[35, 61], [34, 61], [34, 60], [35, 60]]
        gs.wiz3_cord = [[15, 44], [14, 44], [14, 45], [15, 45]]
        gs.buildings_pos.append(gs.town_hall_cord)
        gs.buildings_pos.append(gs.cannon1_cord)
        gs.buildings_pos.append(gs.cannon2_cord)
        gs.buildings_pos.append(gs.cannon3_cord)
        gs.buildings_pos.append(gs.hut1_cord)
        gs.buildings_pos.append(gs.hut2_cord)
        gs.buildings_pos.append(gs.hut3_cord)
        gs.buildings_pos.append(gs.hut4_cord)
        gs.buildings_pos.append(gs.hut5_cord)
        gs.buildings_pos.append(gs.wiz1_cord)
        gs.buildings_pos.append(gs.wiz2_cord)
        gs.buildings_pos.append(gs.wiz3_cord)
        for i in gs.archer_pos:
            gs.board[i[0]][i[1]] = " "
        for i in gs.balloon_pos:
            gs.board[i[0]][i[1]] = " "
        for i in gs.troops_pos:
            gs.board[i[0]][i[1]] = " "
        gs.board[gs.king_pos[0]][gs.king_pos[1]] = " "
        gs.building[gs.king_pos[0]][gs.king_pos[1]] = " "

        gs.troops_pos = []
        gs.troopss = []
        gs.archer_pos = []
        gs.balloon_pos = []
        gs.archers = []
        gs.balloons = []
        gs.king_pos = [25, 26]
        gs.cannon1_pos = [25, 35]
        gs.cannon2_pos = [25, 71]
        gs.cannon3_pos = [17, 51]
        gs.cannon4_pos = [35, 56]
        gs.wiz1_pos = [15, 63]
        gs.wiz2_pos = [35, 61]
        gs.wiz3_pos = [15, 44]
        gs.wiz4_pos = [35, 41]
        gs.hut1_pos = [15, 71]
        gs.TH_HEALTH = 150
        gs.KING_ATTACK = 30
        gs.KING_HEALTH = 1000
        gs.KING_SPEED = 1
        gs.HUT_HEALTH = [70, 70, 70, 70, 70]
        gs.BARBARIAN_HEALTH = 50
        gs.BARBARIAN_ATTACK = 20
        gs.CANNON_ATTACK = 30
        gs.CANNON1_HEALTH = 100
        gs.CANNON2_HEALTH = 100
        gs.CANNON3_HEALTH = 100
        gs.CANNON4_HEALTH = 100
        gs.WIZARD_ATTACK = 30
        gs.WIZARD_HEALTH = [100, 100, 100, 100]
        gs.th_destroyed = 0
        gs.cannon1_destroyed = 0
        gs.cannon2_destroyed = 0
        gs.cannon3_destroyed = 0
        gs.cannon4_destroyed = 0
        gs.hut_destroyed1 = 0
        gs.hut_destroyed2 = 0
        gs.hut_destroyed3 = 0
        gs.hut_destroyed4 = 0
        gs.hut_destroyed5 = 0
        gs.wiz_destroyed1 = 0
        gs.wiz_destroyed2 = 0
        gs.wiz_destroyed3 = 0
        gs.wiz_destroyed4 = 0
        gs.king_destroyed = 0
        gs.BARBARIAN_COUNT = 0
        gs.ARCHER_COUNT = 0
        gs.BALLOON_COUNT = 0

    elif gs.level == 3 and gs.runonce3 == 0:
        gs.runonce3 = 1
        gs.building_alive = 14
        base.townhall("GREEN")
        base.wall()
        base.cannon(1, "GREEN")
        base.cannon(2, "GREEN")
        base.cannon(3, "GREEN")
        base.cannon(4, "GREEN")
        base.hut(1, "GREEN")
        base.hut(2, "GREEN")
        base.hut(3, "GREEN")
        base.hut(4, "GREEN")
        base.hut(5, "GREEN")
        base.wizard_tower(1, "GREEN")
        base.wizard_tower(2, "GREEN")
        base.wizard_tower(3, "GREEN")
        base.wizard_tower(4, "GREEN")
        base.spawn_point()
        base.boundary()
        king.update()
        for j in range(4):
            j = j + 50
            for i in range(3):
                i = i + 25
                gs.town_hall_cord.append([i, j])
        gs.cannon1_cord = [[25, 35], [24, 34], [24, 35], [25, 34]]
        gs.cannon2_cord = [[25, 71], [24, 71], [24, 70], [25, 70]]
        gs.cannon3_cord = [[17, 51], [18, 51], [18, 50], [17, 50]]
        gs.cannon4_cord = [[35, 56], [34, 56], [34, 55], [35, 55]]
        gs.hut1_cord = [[15, 71], [14, 71], [14, 70], [15, 70]]
        gs.hut2_cord = [[35, 71], [34, 71], [34, 70], [35, 70]]
        gs.hut3_cord = [[15, 34], [14, 34], [14, 35], [15, 35]]
        gs.hut4_cord = [[15, 55], [14, 55], [14, 54], [15, 54]]
        gs.hut5_cord = [[35, 51], [34, 51], [34, 50], [35, 50]]
        gs.wiz1_cord = [[15, 63], [14, 63], [14, 62], [15, 62]]
        gs.wiz2_cord = [[35, 61], [34, 61], [34, 60], [35, 60]]
        gs.wiz3_cord = [[15, 44], [14, 44], [14, 45], [15, 45]]
        gs.wiz4_cord = [[35, 41], [34, 41], [34, 40], [35, 40]]
        gs.buildings_pos.append(gs.town_hall_cord)
        gs.buildings_pos.append(gs.cannon1_cord)
        gs.buildings_pos.append(gs.cannon2_cord)
        gs.buildings_pos.append(gs.cannon3_cord)
        gs.buildings_pos.append(gs.cannon4_cord)
        gs.buildings_pos.append(gs.hut1_cord)
        gs.buildings_pos.append(gs.hut2_cord)
        gs.buildings_pos.append(gs.hut3_cord)
        gs.buildings_pos.append(gs.hut4_cord)
        gs.buildings_pos.append(gs.hut5_cord)
        gs.buildings_pos.append(gs.wiz1_cord)
        gs.buildings_pos.append(gs.wiz2_cord)
        gs.buildings_pos.append(gs.wiz3_cord)
        gs.buildings_pos.append(gs.wiz4_cord)
        for i in gs.archer_pos:
            gs.board[i[0]][i[1]] = " "
        for i in gs.balloon_pos:
            gs.board[i[0]][i[1]] = " "
        for i in gs.troops_pos:
            gs.board[i[0]][i[1]] = " "
        gs.board[gs.king_pos[0]][gs.king_pos[1]] = " "
        gs.building[gs.king_pos[0]][gs.king_pos[1]] = " "

        gs.king_pos = [25, 26]
        gs.cannon1_pos = [25, 35]
        gs.cannon2_pos = [25, 71]
        gs.cannon3_pos = [17, 51]
        gs.cannon4_pos = [35, 56]
        gs.wiz1_pos = [15, 63]
        gs.wiz2_pos = [35, 61]
        gs.wiz3_pos = [15, 44]
        gs.wiz4_pos = [35, 41]

    inp = input_to(Get())
    health.check_health()
    cannon.attack()
    wizard.attack()
    for i in gs.troopss:
        i.move()
    for i in gs.archers:
        i.move()
    for i in gs.balloons:
        i.move()
    if inp == None:
        pass
    elif inp == "w" or inp == "W":
        last_direction = "w"
        file1.write(inp + "\n")
        king.movement("UP")
    elif inp == "a" or inp == "A":
        last_direction = "a"
        file1.write(inp + "\n")
        king.movement("LEFT")
    elif inp == "s" or inp == "S":
        last_direction = "s"
        file1.write(inp + "\n")
        king.movement("DOWN")
    elif inp == "d" or inp == "D":
        last_direction = "d"
        file1.write(inp + "\n")
        king.movement("RIGHT")
    elif inp == " " and ki == 1:
        file1.write(inp + "\n")
        king.attack(ki,last_direction)
    elif inp == " ":
        file1.write(inp + "\n")
        king.attack(ki,last_direction)
    elif inp == "i" or inp == "o" or inp == "p":
        file1.write(inp + "\n")
        T = Troops()
        T.spawn(inp)
        gs.troopss.append(T)
    elif inp == "j" or inp == "k" or inp == "l":
        file1.write(inp + "\n")
        T = Archers()
        T.spawn(inp)
        gs.archers.append(T)
    elif inp == "b" or inp == "n" or inp == "m":
        T = Balloons()
        T.spawn(inp)
        gs.balloons.append(T)
    elif inp == "q" or inp == "Q":
        file1.write(inp + "\n")
        Get().show_cursor()
        os.system("clear")
        file1.close()
        exit()
    elif inp == "r" or inp == "h":
        file1.write(inp + "\n")
        spel = Spell()
        spel.cast(inp)
    os.system("clear")
    # print(gs.board[gs.king_pos[0]][gs.king_pos[1]])
    for x in gs.board:
        for i in x:
            if(i == Fore.WHITE + "K" and ki == 2):
                print(Fore.WHITE + "Q",end=" ")
            else:
                print(i, end=" ")
        print()
    # print(gs.board[gs.king_pos[0]][gs.king_pos[1]])
