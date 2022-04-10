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
import os.path
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

for i in range(1000):
    if os.path.exists("replays/no" + str(i)):
        continue
    else:
        file1 = open("replays/no" + str(i), "a")
        break

while True:
    inp = input_to(Get())
    health.check_health()
    cannon.attack()
    for i in gs.troopss:   
        i.move()
    if inp == None:
        pass
    elif inp == "w" or inp == "W":
        file1.write(inp + "\n")
        king.movement("UP")
    elif inp == "a" or inp == "A":
        file1.write(inp + "\n")
        king.movement("LEFT")
    elif inp == "s" or inp == "S":
        file1.write(inp + "\n")
        king.movement("DOWN")
    elif inp == "d" or inp == "D":
        file1.write(inp + "\n")
        king.movement("RIGHT")
    elif inp == " ":
        file1.write(inp + "\n")
        king.attack()
    elif inp == "i" or inp == "o" or inp == "p":
        file1.write(inp + "\n")
        T = Troops()
        T.spawn(inp)
        gs.troopss.append(T)
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

    for x in gs.board:
        for i in x:
            print(i, end=" ")
        print()

# os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
# os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
