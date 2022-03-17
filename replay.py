from input import Get, input_to
from colorama import init, Fore, Back, Style
import os
import global_stuff as gs
from base import Base
from king import King
from troops import Troops
from cannon import Cannon
from health import Health
import os.path
import sys
import time

init()

Get().hide_cursor()
os.system("clear")

base = Base()
king = King()
cannon = Cannon()
health = Health()
base.townhall("GREEN")
base.wall()
base.cannon(1, "GREEN")
base.cannon(2, "GREEN")
base.hut(1, "GREEN")
base.hut(2, "GREEN")
base.hut(3, "GREEN")
base.hut(4, "GREEN")
base.hut(5, "GREEN")
base.spawn_point()
base.boundary()
king.update()
for j in range(4):
    j = j + 50
    for i in range(3):
        i = i + 25
        gs.town_hall_cord.append([i,j])
gs.cannon1_cord = [[25,35],[24,34],[24,35],[25,34]]
gs.cannon2_cord = [[25,71],[24,71],[24,70],[25,70]]
gs.hut1_cord = [[15,71],[14,71],[14,70],[15,70]]
gs.hut2_cord = [[35,71],[34,71],[34,70],[35,70]]
gs.hut3_cord = [[15,34],[14,34],[14,35],[15,35]]
gs.hut4_cord = [[15,55],[14,55],[14,54],[15,54]]
gs.hut5_cord = [[35,51],[34,51],[34,50],[35,50]]
gs.buildings_pos.append(gs.town_hall_cord)
gs.buildings_pos.append(gs.cannon1_cord)
gs.buildings_pos.append(gs.cannon2_cord)
gs.buildings_pos.append(gs.hut1_cord)
gs.buildings_pos.append(gs.hut2_cord)
gs.buildings_pos.append(gs.hut3_cord)
gs.buildings_pos.append(gs.hut4_cord)
gs.buildings_pos.append(gs.hut5_cord)



if sys.argv[1]=="help":
    print("Usage: python replay.py <number>")
    Get().show_cursor()
    exit()
else:
    file1 = open("replays/no" + str(sys.argv[1]), 'r')
    Lines = file1.readlines()
count = 0
while True:
    if count >= len(Lines):
        inp=""
    else:
        inp = Lines[count][0]
    count += 1


    health.check_health()
    cannon.attack()
    for i in gs.troopss:   
        i.move()
    if inp == None:
        pass
    elif inp == "w" or inp == "W":
        king.movement("UP")
    elif inp == "a" or inp == "A":
        king.movement("LEFT")
    elif inp == "s" or inp == "S":
        king.movement("DOWN")
    elif inp == "d" or inp == "D":
        king.movement("RIGHT")
    elif inp == " ":
        king.attack()
    elif inp == "i" or inp == "o" or inp == "p":
        T = Troops()
        T.spawn(inp)
        gs.troopss.append(T)
    elif inp == "q" or inp == "Q":
        Get().show_cursor()
        os.system("clear")
        file1.close()
        exit()
    os.system("clear")
    for x in gs.board:
        for i in x:
            print(i, end=" ")
        print()
    time.sleep(0.5)