from colorama import init, Fore, Back, Style
import global_stuff as gs
from base import Base
import os
from input import Get, input_to
init()
base = Base()


class Health:
    def check_health(self):
        if gs.KING_HEALTH <= 0:
            current_health = ' ' * int((1000 - int(gs.KING_HEALTH))/int(100))
            remaining_health = ' ' * int(int(gs.KING_HEALTH)/int(100))
            gs.board[0][0]="King's Health : |" + Back.GREEN + remaining_health + Back.RED + current_health + Back.RESET + "|"
            gs.king_destroyed += 1
            gs.board[gs.king_pos[0]][gs.king_pos[1]] = Fore.WHITE + "D"
        else:
            current_health = ' ' * int((1000 - int(gs.KING_HEALTH))/int(100))
            remaining_health = ' ' * int(int(gs.KING_HEALTH)/int(100))
            gs.board[0][0]="King's Health : |" + Back.GREEN + remaining_health + Back.RED + current_health + Back.RESET + "|"
        if gs.king_destroyed == 1:
            gs.troop_alive=gs.troop_alive-1
            gs.king_destroyed += 1
        if gs.TH_HEALTH <= 0:
            base.townhall("RESET")
            gs.th_destroyed += 1
            if gs.town_hall_cord in gs.buildings_pos:
                gs.buildings_pos.remove(gs.town_hall_cord)
        if gs.th_destroyed == 1:
            gs.building_alive=gs.building_alive-1
            gs.th_destroyed += 1
        if gs.TH_HEALTH <= 40 and gs.TH_HEALTH > 0:
            base.townhall("RED")
        if gs.TH_HEALTH > 40 and gs.TH_HEALTH <= 100:
            base.townhall("YELLOW")

        if gs.CANNON1_HEALTH <= 0:
            base.cannon(1, "RESET")
            gs.cannon1_destroyed += 1
            if gs.cannon1_cord in gs.buildings_pos:
                gs.buildings_pos.remove(gs.cannon1_cord)
        if gs.cannon1_destroyed == 1:
            gs.building_alive=gs.building_alive-1
            gs.cannon1_destroyed += 1
        if gs.CANNON1_HEALTH <= 30 and gs.CANNON1_HEALTH > 0:
            base.cannon(1, "RED")
        if gs.CANNON1_HEALTH > 30 and gs.CANNON1_HEALTH <= 60:
            base.cannon(1, "YELLOW")

        if gs.CANNON2_HEALTH <= 0:
            base.cannon(2, "RESET")
            gs.cannon2_destroyed += 1
            if gs.cannon2_cord in gs.buildings_pos:
                gs.buildings_pos.remove(gs.cannon2_cord)
        if gs.cannon2_destroyed == 1:
            gs.building_alive=gs.building_alive-1
            gs.cannon2_destroyed += 1
        if gs.CANNON2_HEALTH <= 30 and gs.CANNON2_HEALTH > 0:
            base.cannon(2, "RED")
        if gs.CANNON2_HEALTH > 30 and gs.CANNON2_HEALTH <= 60:
            base.cannon(2, "YELLOW")
        for i in range(5):
            if gs.HUT_HEALTH[i] <= 0:
                base.hut(i + 1, "RESET")
                if i == 0:
                    gs.hut_destroyed1 += 1
                    if gs.hut1_cord in gs.buildings_pos:
                        gs.buildings_pos.remove(gs.hut1_cord)
                elif i == 1:
                    gs.hut_destroyed2 += 1
                    if gs.hut2_cord in gs.buildings_pos:
                        gs.buildings_pos.remove(gs.hut2_cord)
                elif i == 2:
                    gs.hut_destroyed3 += 1
                    if gs.hut3_cord in gs.buildings_pos:
                        gs.buildings_pos.remove(gs.hut3_cord)
                elif i == 3:
                    gs.hut_destroyed4 += 1
                    if gs.hut4_cord in gs.buildings_pos:
                        gs.buildings_pos.remove(gs.hut4_cord)
                elif i == 4:
                    gs.hut_destroyed5 += 1
                    if gs.hut5_cord in gs.buildings_pos:
                        gs.buildings_pos.remove(gs.hut5_cord)
            if gs.HUT_HEALTH[i] <= 30 and gs.HUT_HEALTH[i] > 0:
                base.hut(i + 1, "RED")
            if gs.HUT_HEALTH[i] > 30 and gs.HUT_HEALTH[i] <= 60:
                base.hut(i + 1, "YELLOW")
        if gs.hut_destroyed1 == 1:
            gs.building_alive=gs.building_alive-1
            gs.hut_destroyed1 += 1
        if gs.hut_destroyed2 == 1:
            gs.building_alive=gs.building_alive-1
            gs.hut_destroyed2 += 1
        if gs.hut_destroyed3 == 1:
            gs.building_alive=gs.building_alive-1
            gs.hut_destroyed3 += 1
        if gs.hut_destroyed4 == 1:
            gs.building_alive=gs.building_alive-1
            gs.hut_destroyed4 += 1
        if gs.hut_destroyed5 == 1:
            gs.building_alive=gs.building_alive-1
            gs.hut_destroyed5 += 1
        for i in gs.troopss:
            if i.health <= 0:
                if [i.x, i.y] in gs.troops_pos:
                    gs.troops_pos.remove([i.x, i.y])
                    gs.board[i.x][i.y] = " "
                    gs.troopss.remove(i)

        if gs.troop_alive == 0 and len(gs.troopss) == 0:
            os.system("clear")
            os.system('aplay -q ./sounds/lose.wav& 2>/dev/null')
            print(Fore.RED + r"""            
             **    **   *******   **     **   **         *******    ******** ********
            //**  **   **/////** /**    /**  /**        **/////**  **////// /**///// 
             //****   **     //**/**    /**  /**       **     //**/**       /**      
              //**   /**      /**/**    /**  /**      /**      /**/*********/******* 
               /**   /**      /**/**    /**  /**      /**      /**////////**/**////  
               /**   //**     ** /**    /**  /**      //**     **        /**/**      
               /**    //*******  //*******   /******** //*******   ******** /********
               //      ///////    ///////    ////////   ///////   ////////  //////// 
       """)
            print()
            

            Get().show_cursor()
            exit()
        if gs.building_alive == 0:
            os.system("clear")
            os.system('aplay -q ./sounds/win.wav& 2>/dev/null')
            print(Fore.GREEN + r"""
                       **    **   *******   **     **   **       **   *******   ****     **
                      //**  **   **/////** /**    /**  /**      /**  **/////** /**/**   /**
                       //****   **     //**/**    /**  /**   *  /** **     //**/**//**  /**
                        //**   /**      /**/**    /**  /**  *** /**/**      /**/** //** /**
                         /**   /**      /**/**    /**  /** **/**/**/**      /**/**  //**/**
                         /**   //**     ** /**    /**  /**** //****//**     ** /**   //****
                         /**    //*******  //*******   /**/   ///** //*******  /**    //***
                         //      ///////    ///////    //       //   ///////   //      /// """)
            Get().show_cursor()
            exit()