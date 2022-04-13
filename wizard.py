from time import sleep
from colorama import init, Fore, Back, Style
import global_stuff as gs
from troops import Troops
import os

init()


class Wizard():
    def attack(self):

        if gs.WIZARD_HEALTH[0] > 0:
            x1 = gs.wiz1_pos[0]
            x2 = gs.wiz1_pos[1]
            y1 = gs.king_pos[0]
            y2 = gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH > 0:
                os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                gs.KING_HEALTH = gs.KING_HEALTH - gs.WIZARD_ATTACK
                for trp in gs.troopss:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.troops_pos:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.archer_pos:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

            else:
                for trp in gs.troopss:
                    x1 = gs.wiz1_pos[0]
                    x2 = gs.wiz1_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.troops_pos:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    x1 = gs.wiz1_pos[0]
                    x2 = gs.wiz1_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.archer_pos:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

        if gs.WIZARD_HEALTH[1] > 0:
            x1 = gs.wiz2_pos[0]
            x2 = gs.wiz2_pos[1]
            y1 = gs.king_pos[0]
            y2 = gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH > 0:
                os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                gs.KING_HEALTH = gs.KING_HEALTH - gs.WIZARD_ATTACK
                for trp in gs.troopss:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.troops_pos:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.archer_pos:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

            else:
                for trp in gs.troopss:
                    x1 = gs.wiz2_pos[0]
                    x2 = gs.wiz2_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.troops_pos and trp.health <= 0:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    x1 = gs.wiz2_pos[0]
                    x2 = gs.wiz2_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.archer_pos and trp.health <= 0:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

        if gs.WIZARD_HEALTH[2] > 0 and gs.level >= 2:
            x1 = gs.wiz3_pos[0]
            x2 = gs.wiz3_pos[1]
            y1 = gs.king_pos[0]
            y2 = gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH > 0:
                os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                gs.KING_HEALTH = gs.KING_HEALTH - gs.WIZARD_ATTACK
                for trp in gs.troopss:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.troops_pos:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.archer_pos:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

            else:
                for trp in gs.troopss:
                    x1 = gs.wiz3_pos[0]
                    x2 = gs.wiz3_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.troops_pos and trp.health <= 0:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    x1 = gs.wiz3_pos[0]
                    x2 = gs.wiz3_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.archer_pos and trp.health <= 0:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

        if gs.WIZARD_HEALTH[3] > 0 and gs.level == 3:
            x1 = gs.wiz4_pos[0]
            x2 = gs.wiz4_pos[1]
            y1 = gs.king_pos[0]
            y2 = gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH > 0:
                os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                gs.KING_HEALTH = gs.KING_HEALTH - gs.WIZARD_ATTACK
                for trp in gs.troopss:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.troops_pos:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    y11 = trp.x
                    y22 = trp.y
                    if (y1-1==y11 and y2-1 == y22) or (y1-1==y11 and y2==y22) or (y1-1==y11 and y2+1 == y22) or (y1 == y11 and y2-1 == y22) or (y1==y11 and y2+1 == y22) or (y1+1==y11 and y2-1 == y22) or (y1+1==y11 and y2 == y22) or (y1+1==y11 and y2+1 == y22):
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp.health <= 0 and trp in gs.archer_pos:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "

            else:
                for trp in gs.troopss:
                    x1 = gs.wiz4_pos[0]
                    x2 = gs.wiz4_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.troops_pos and trp.health <= 0:
                            gs.troops_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
                for trp in gs.archers:
                    x1 = gs.wiz4_pos[0]
                    x2 = gs.wiz4_pos[1]
                    y1 = trp.x
                    y2 = trp.y
                    distance = abs(x1 - y1) + abs(x2 - y2)
                    if distance <= 6 and trp.health > 0:
                        os.system("aplay -q ./sounds/bullet.wav& 2>/dev/null")
                        trp.health = trp.health - gs.WIZARD_ATTACK
                        gs.board[trp.x][trp.y] = Fore.WHITE + "B"
                        if trp in gs.archer_pos and trp.health <= 0:
                            gs.archer_pos.remove(trp)
                        gs.board[trp.x][trp.y] = Fore.WHITE + " "
