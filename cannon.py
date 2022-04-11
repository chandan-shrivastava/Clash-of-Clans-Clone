from time import sleep
from colorama import init, Fore, Back, Style
import global_stuff as gs
from troops import Troops
import os
init()
class Cannon:
    def attack(self):
        if gs.CANNON1_HEALTH > 0:
            x1=gs.cannon1_pos[0]
            x2=gs.cannon1_pos[1]
            y1=gs.king_pos[0]
            y2=gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH>0:
                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                gs.KING_HEALTH = gs.KING_HEALTH - gs.CANNON_ATTACK
            for trp in gs.troopss:
                x1=gs.cannon1_pos[0]
                x2=gs.cannon1_pos[1]
                y1=trp.x
                y2=trp.y
                distance = abs(x1 - y1) + abs(x2 - y2)
                if distance <= 6 and trp.health>0:
                    os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                    trp.health = trp.health - gs.CANNON_ATTACK
                    gs.board[trp.x][trp.y] = Fore.WHITE + "B" # + str(trp.health)
                    if trp.health <= 0 and trp in gs.troops_pos:
                        gs.troops_pos.remove(trp)
                    # gs.troops_pos.remove(trp)
                    # sleep(0.5)
                    gs.board[trp.x][trp.y] = Fore.WHITE + " "
        if gs.CANNON2_HEALTH > 0:
            x1=gs.cannon2_pos[0]
            x2=gs.cannon2_pos[1]
            y1=gs.king_pos[0]
            y2=gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH>0:
                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                gs.KING_HEALTH = gs.KING_HEALTH - gs.CANNON_ATTACK
            for trp in gs.troopss:
                x1=gs.cannon1_pos[0]
                x2=gs.cannon1_pos[1]
                y1=trp.x
                y2=trp.y
                distance = abs(x1 - y1) + abs(x2 - y2)
                if distance <= 6 and trp.health>0:
                    os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                    trp.health = trp.health - gs.CANNON_ATTACK
                    gs.board[trp.x][trp.y] = Fore.WHITE + "B" # + str(trp.health)
                    if trp in gs.troops_pos and trp.health <= 0:
                        gs.troops_pos.remove(trp)
                    # gs.troops_pos.remove(trp)
                    # sleep(0.5)
                    gs.board[trp.x][trp.y] = Fore.WHITE + " "\
        
        if gs.CANNON3_HEALTH > 0:
            x1=gs.cannon3_pos[0]
            x2=gs.cannon3_pos[1]
            y1=gs.king_pos[0]
            y2=gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH>0:
                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                gs.KING_HEALTH = gs.KING_HEALTH - gs.CANNON_ATTACK
            for trp in gs.troopss:
                x1=gs.cannon3_pos[0]
                x2=gs.cannon3_pos[1]
                y1=trp.x
                y2=trp.y
                distance = abs(x1 - y1) + abs(x2 - y2)
                if distance <= 6 and trp.health>0:
                    os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                    trp.health = trp.health - gs.CANNON_ATTACK
                    gs.board[trp.x][trp.y] = Fore.WHITE + "B" # + str(trp.health)
                    if trp in gs.troops_pos and trp.health <= 0:
                        gs.troops_pos.remove(trp)
                    # gs.troops_pos.remove(trp)
                    # sleep(0.5)
                    gs.board[trp.x][trp.y] = Fore.WHITE + " "

        if gs.CANNON4_HEALTH > 0:
            x1=gs.cannon4_pos[0]
            x2=gs.cannon4_pos[1]
            y1=gs.king_pos[0]
            y2=gs.king_pos[1]
            distance = abs(x1 - y1) + abs(x2 - y2)
            if distance <= 6 and gs.KING_HEALTH>0:
                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                gs.KING_HEALTH = gs.KING_HEALTH - gs.CANNON_ATTACK
            for trp in gs.troopss:
                x1=gs.cannon4_pos[0]
                x2=gs.cannon4_pos[1]
                y1=trp.x
                y2=trp.y
                distance = abs(x1 - y1) + abs(x2 - y2)
                if distance <= 6 and trp.health>0:
                    os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                    trp.health = trp.health - gs.CANNON_ATTACK
                    gs.board[trp.x][trp.y] = Fore.WHITE + "B" # + str(trp.health)
                    if trp in gs.troops_pos and trp.health <= 0:
                        gs.troops_pos.remove(trp)
                    # gs.troops_pos.remove(trp)
                    # sleep(0.5)
                    gs.board[trp.x][trp.y] = Fore.WHITE + " "