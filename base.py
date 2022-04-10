from colorama import init, Fore, Back, Style

init()
import global_stuff as gs


class Base:
    def boundary(self):
        for i in range(10, 99):
            gs.board[5][i] = Fore.WHITE + "-"
            gs.building[5][i] = "BORDER"
        for i in range(5, 49):
            gs.board[i][10] = Fore.WHITE + "|"
            gs.building[i][10] = "BORDER"
        for i in range(10, 99):
            gs.board[49][i] = Fore.WHITE + "-"
            gs.building[49][i] = "BORDER"
        for i in range(5, 49):
            gs.board[i][99] = Fore.WHITE + "|"
            gs.building[i][99] = "BORDER"

    def townhall(self, color):
        if color == "RED":
            for j in range(4):
                j = j + 50
                for i in range(3):
                    i = i + 25
                    gs.board[i][j] = Fore.RED + "T"
                    gs.building[i][j] = "TH"
        if color == "YELLOW":
            for j in range(4):
                j = j + 50
                for i in range(3):
                    i = i + 25
                    gs.board[i][j] = Fore.YELLOW + "T"
                    gs.building[i][j] = "TH"
        if color == "GREEN":
            for j in range(4):
                j = j + 50
                for i in range(3):
                    i = i + 25
                    gs.board[i][j] = Fore.GREEN + "T"
                    gs.building[i][j] = "TH"
        if color == "RESET":
            for j in range(4):
                j = j + 50
                for i in range(3):
                    i = i + 25
                    gs.board[i][j] = " "
                    gs.building[i][j] = " "

    def cannon(self, no, color):
        if color == "RED":
            if no == 1:
                gs.board[25][35] = Fore.RED + "C"
                gs.board[24][34] = Fore.RED + "C"
                gs.board[24][35] = Fore.RED + "C"
                gs.board[25][34] = Fore.RED + "C"
                gs.building[25][35] = "CANNON1"
                gs.building[24][34] = "CANNON1"
                gs.building[24][35] = "CANNON1"
                gs.building[25][34] = "CANNON1"
            if no == 2:
                gs.board[25][71] = Fore.RED + "C"
                gs.board[24][71] = Fore.RED + "C"
                gs.board[24][70] = Fore.RED + "C"
                gs.board[25][70] = Fore.RED + "C"
                gs.building[25][71] = "CANNON2"
                gs.building[24][71] = "CANNON2"
                gs.building[24][70] = "CANNON2"
                gs.building[25][70] = "CANNON2"

        if color == "YELLOW":
            if no == 1:
                gs.board[25][35] = Fore.YELLOW + "C"
                gs.board[24][34] = Fore.YELLOW + "C"
                gs.board[24][35] = Fore.YELLOW + "C"
                gs.board[25][34] = Fore.YELLOW + "C"
                gs.building[25][35] = "CANNON1"
                gs.building[24][34] = "CANNON1"
                gs.building[24][35] = "CANNON1"
                gs.building[25][34] = "CANNON1"
            if no == 2:
                gs.board[25][71] = Fore.YELLOW + "C"
                gs.board[24][71] = Fore.YELLOW + "C"
                gs.board[24][70] = Fore.YELLOW + "C"
                gs.board[25][70] = Fore.YELLOW + "C"
                gs.building[25][71] = "CANNON2"
                gs.building[24][71] = "CANNON2"
                gs.building[24][70] = "CANNON2"
                gs.building[25][70] = "CANNON2"

        if color == "GREEN":
            if no == 1:
                gs.board[25][35] = Fore.GREEN + "C"
                gs.board[24][34] = Fore.GREEN + "C"
                gs.board[24][35] = Fore.GREEN + "C"
                gs.board[25][34] = Fore.GREEN + "C"
                gs.building[25][35] = "CANNON1"
                gs.building[24][34] = "CANNON1"
                gs.building[24][35] = "CANNON1"
                gs.building[25][34] = "CANNON1"
            if no == 2:
                gs.board[25][71] = Fore.GREEN + "C"
                gs.board[24][71] = Fore.GREEN + "C"
                gs.board[24][70] = Fore.GREEN + "C"
                gs.board[25][70] = Fore.GREEN + "C"
                gs.building[25][71] = "CANNON2"
                gs.building[24][71] = "CANNON2"
                gs.building[24][70] = "CANNON2"
                gs.building[25][70] = "CANNON2"

        if color == "RESET":
            if no == 1:
                gs.board[25][35] = " "
                gs.board[24][34] = " "
                gs.board[24][35] = " "
                gs.board[25][34] = " "
                gs.building[25][35] = " "
                gs.building[24][34] = " "
                gs.building[24][35] = " "
                gs.building[25][34] = " "
            if no == 2:
                gs.board[25][71] = " "
                gs.board[24][71] = " "
                gs.board[24][70] = " "
                gs.board[25][70] = " "
                gs.building[25][71] = " "
                gs.building[24][71] = " "
                gs.building[24][70] = " "
                gs.building[25][70] = " "

    def hut(self, no, color):
        if color == "RED":
            if no == 1:
                gs.board[15][71] = Fore.RED + "H"
                gs.board[14][71] = Fore.RED + "H"
                gs.board[14][70] = Fore.RED + "H"
                gs.board[15][70] = Fore.RED + "H"
                gs.building[15][71] = "HUTS1"
                gs.building[14][71] = "HUTS1"
                gs.building[14][70] = "HUTS1"
                gs.building[15][70] = "HUTS1"
            if no == 2:
                gs.board[35][71] = Fore.RED + "H"
                gs.board[34][71] = Fore.RED + "H"
                gs.board[34][70] = Fore.RED + "H"
                gs.board[35][70] = Fore.RED + "H"
                gs.building[35][71] = "HUTS2"
                gs.building[34][71] = "HUTS2"
                gs.building[34][70] = "HUTS2"
                gs.building[35][70] = "HUTS2"
            if no == 3:
                gs.board[15][34] = Fore.RED + "H"
                gs.board[14][34] = Fore.RED + "H"
                gs.board[14][35] = Fore.RED + "H"
                gs.board[15][35] = Fore.RED + "H"
                gs.building[15][34] = "HUTS3"
                gs.building[14][34] = "HUTS3"
                gs.building[14][35] = "HUTS3"
                gs.building[15][35] = "HUTS3"
            if no == 4:
                gs.board[15][55] = Fore.RED + "H"
                gs.board[14][55] = Fore.RED + "H"
                gs.board[14][54] = Fore.RED + "H"
                gs.board[15][54] = Fore.RED + "H"
                gs.building[15][55] = "HUTS4"
                gs.building[14][55] = "HUTS4"
                gs.building[14][54] = "HUTS4"
                gs.building[15][54] = "HUTS4"
            if no == 5:
                gs.board[35][51] = Fore.RED + "H"
                gs.board[34][51] = Fore.RED + "H"
                gs.board[34][50] = Fore.RED + "H"
                gs.board[35][50] = Fore.RED + "H"
                gs.building[35][51] = "HUTS5"
                gs.building[34][51] = "HUTS5"
                gs.building[34][50] = "HUTS5"
                gs.building[35][50] = "HUTS5"

        if color == "YELLOW":
            if no == 1:
                gs.board[15][71] = Fore.YELLOW + "H"
                gs.board[14][71] = Fore.YELLOW + "H"
                gs.board[14][70] = Fore.YELLOW + "H"
                gs.board[15][70] = Fore.YELLOW + "H"
                gs.building[15][71] = "HUTS1"
                gs.building[14][71] = "HUTS1"
                gs.building[14][70] = "HUTS1"
                gs.building[15][70] = "HUTS1"
            if no == 2:
                gs.board[35][71] = Fore.YELLOW + "H"
                gs.board[34][71] = Fore.YELLOW + "H"
                gs.board[34][70] = Fore.YELLOW + "H"
                gs.board[35][70] = Fore.YELLOW + "H"
                gs.building[35][71] = "HUTS2"
                gs.building[34][71] = "HUTS2"
                gs.building[34][70] = "HUTS2"
                gs.building[35][70] = "HUTS2"
            if no == 3:
                gs.board[15][34] = Fore.YELLOW + "H"
                gs.board[14][34] = Fore.YELLOW + "H"
                gs.board[14][35] = Fore.YELLOW + "H"
                gs.board[15][35] = Fore.YELLOW + "H"
                gs.building[15][34] = "HUTS3"
                gs.building[14][34] = "HUTS3"
                gs.building[14][35] = "HUTS3"
                gs.building[15][35] = "HUTS3"
            if no == 4:
                gs.board[15][55] = Fore.YELLOW + "H"
                gs.board[14][55] = Fore.YELLOW + "H"
                gs.board[14][54] = Fore.YELLOW + "H"
                gs.board[15][54] = Fore.YELLOW + "H"
                gs.building[15][55] = "HUTS4"
                gs.building[14][55] = "HUTS4"
                gs.building[14][54] = "HUTS4"
                gs.building[15][54] = "HUTS4"
            if no == 5:
                gs.board[35][51] = Fore.YELLOW + "H"
                gs.board[34][51] = Fore.YELLOW + "H"
                gs.board[34][50] = Fore.YELLOW + "H"
                gs.board[35][50] = Fore.YELLOW + "H"
                gs.building[35][51] = "HUTS5"
                gs.building[34][51] = "HUTS5"
                gs.building[34][50] = "HUTS5"
                gs.building[35][50] = "HUTS5"

        if color == "GREEN":
            if no == 1:
                gs.board[15][71] = Fore.GREEN + "H"
                gs.board[14][71] = Fore.GREEN + "H"
                gs.board[14][70] = Fore.GREEN + "H"
                gs.board[15][70] = Fore.GREEN + "H"
                gs.building[15][71] = "HUTS1"
                gs.building[14][71] = "HUTS1"
                gs.building[14][70] = "HUTS1"
                gs.building[15][70] = "HUTS1"
            if no == 2:
                gs.board[35][71] = Fore.GREEN + "H"
                gs.board[34][71] = Fore.GREEN + "H"
                gs.board[34][70] = Fore.GREEN + "H"
                gs.board[35][70] = Fore.GREEN + "H"
                gs.building[35][71] = "HUTS2"
                gs.building[34][71] = "HUTS2"
                gs.building[34][70] = "HUTS2"
                gs.building[35][70] = "HUTS2"
            if no == 3:
                gs.board[15][34] = Fore.GREEN + "H"
                gs.board[14][34] = Fore.GREEN + "H"
                gs.board[14][35] = Fore.GREEN + "H"
                gs.board[15][35] = Fore.GREEN + "H"
                gs.building[15][34] = "HUTS3"
                gs.building[14][34] = "HUTS3"
                gs.building[14][35] = "HUTS3"
                gs.building[15][35] = "HUTS3"
            if no == 4:
                gs.board[15][55] = Fore.GREEN + "H"
                gs.board[14][55] = Fore.GREEN + "H"
                gs.board[14][54] = Fore.GREEN + "H"
                gs.board[15][54] = Fore.GREEN + "H"
                gs.building[15][55] = "HUTS4"
                gs.building[14][55] = "HUTS4"
                gs.building[14][54] = "HUTS4"
                gs.building[15][54] = "HUTS4"
            if no == 5:
                gs.board[35][51] = Fore.GREEN + "H"
                gs.board[34][51] = Fore.GREEN + "H"
                gs.board[34][50] = Fore.GREEN + "H"
                gs.board[35][50] = Fore.GREEN + "H"
                gs.building[35][51] = "HUTS5"
                gs.building[34][51] = "HUTS5"
                gs.building[34][50] = "HUTS5"
                gs.building[35][50] = "HUTS5"
        if color == "RESET":
            if no == 1:
                gs.board[15][71] = " "
                gs.board[14][71] = " "
                gs.board[14][70] = " "
                gs.board[15][70] = " "
                gs.building[15][71] = " "
                gs.building[14][71] = " "
                gs.building[14][70] = " "
                gs.building[15][70] = " "
            if no == 2:
                gs.board[35][71] = " "
                gs.board[34][71] = " "
                gs.board[34][70] = " "
                gs.board[35][70] = " "
                gs.building[35][71] = " "
                gs.building[34][71] = " "
                gs.building[34][70] = " "
                gs.building[35][70] = " "
            if no == 3:
                gs.board[15][34] = " "
                gs.board[14][34] = " "
                gs.board[14][35] = " "
                gs.board[15][35] = " "
                gs.building[15][34] = " "
                gs.building[14][34] = " "
                gs.building[14][35] = " "
                gs.building[15][35] = " "
            if no == 4:
                gs.board[15][55] = " "
                gs.board[14][55] = " "
                gs.board[14][54] = " "
                gs.board[15][54] = " "
                gs.building[15][55] = " "
                gs.building[14][55] = " "
                gs.building[14][54] = " "
                gs.building[15][54] = " "
            if no == 5:
                gs.board[35][51] = " "
                gs.board[34][51] = " "
                gs.board[34][50] = " "
                gs.board[35][50] = " "
                gs.building[35][51] = " "
                gs.building[34][51] = " "
                gs.building[34][50] = " "
                gs.building[35][50] = " "

    def wall(self):
        for i in range(12):
            i = i + 20
            gs.board[i][45] = Fore.RED + "W"
            gs.building[i][45] = "WALLS"
        for i in range(12):
            i = i + 20
            gs.board[i][60] = Fore.RED + "W"
            gs.building[i][60] = "WALLS"
        for i in range(15):
            i = i + 45
            gs.board[20][i] = Fore.RED + "W"
            gs.building[20][i] = "WALLS"
        for i in range(15):
            i = i + 45
            gs.board[31][i] = Fore.RED + "W"
            gs.building[31][i] = "WALLS"

    def spawn_point(self):
        gs.board[10][45] = Fore.BLUE + "I"
        gs.board[30][20] = Fore.BLUE + "O"
        gs.board[41][50] = Fore.BLUE + "P"
        gs.building[10][45] = "SPAWN"
        gs.building[30][20] = "SPAWN"
        gs.building[41][50] = "SPAWN"


    def wizard_tower(self, no, color):
        if color == "RED":
            if no == 1:
                gs.board[15][63] = Fore.RED + "W"
                gs.board[14][63] = Fore.RED + "W"
                gs.board[14][62] = Fore.RED + "W"
                gs.board[15][62] = Fore.RED + "W"
                gs.building[15][63] = "WIZARD1"
                gs.building[14][63] = "WIZARD1"
                gs.building[14][62] = "WIZARD1"
                gs.building[15][62] = "WIZARD1"
            if no == 2:
                gs.board[35][61] = Fore.RED + "W"
                gs.board[34][61] = Fore.RED + "W"
                gs.board[34][60] = Fore.RED + "W"
                gs.board[35][60] = Fore.RED + "W"
                gs.building[35][61] = "WIZARD2"
                gs.building[34][61] = "WIZARD2"
                gs.building[34][60] = "WIZARD2"
                gs.building[35][60] = "WIZARD2"
            if no == 3:
                gs.board[15][44] = Fore.RED + "W"
                gs.board[14][44] = Fore.RED + "W"
                gs.board[14][45] = Fore.RED + "W"
                gs.board[15][45] = Fore.RED + "W"
                gs.building[15][44] = "WIZARD3"
                gs.building[14][44] = "WIZARD3"
                gs.building[14][45] = "WIZARD3"
                gs.building[15][45] = "WIZARD3"
            if no == 4:
                gs.board[35][41] = Fore.RED + "W"
                gs.board[34][41] = Fore.RED + "W"
                gs.board[34][40] = Fore.RED + "W"
                gs.board[35][40] = Fore.RED + "W"
                gs.building[35][41] = "WIZARD4"
                gs.building[34][41] = "WIZARD4"
                gs.building[34][40] = "WIZARD4"
                gs.building[35][40] = "WIZARD4"

        if color == "YELLOW":
            if no == 1:
                gs.board[15][63] = Fore.YELLOW + "W"
                gs.board[14][63] = Fore.YELLOW + "W"
                gs.board[14][62] = Fore.YELLOW + "W"
                gs.board[15][62] = Fore.YELLOW + "W"
                gs.building[15][63] = "WIZARD1"
                gs.building[14][63] = "WIZARD1"
                gs.building[14][62] = "WIZARD1"
                gs.building[15][62] = "WIZARD1"
            if no == 2:
                gs.board[35][61] = Fore.YELLOW + "W"
                gs.board[34][61] = Fore.YELLOW + "W"
                gs.board[34][60] = Fore.YELLOW + "W"
                gs.board[35][60] = Fore.YELLOW + "W"
                gs.building[35][61] = "WIZARD2"
                gs.building[34][61] = "WIZARD2"
                gs.building[34][60] = "WIZARD2"
                gs.building[35][60] = "WIZARD2"
            if no == 3:
                gs.board[15][44] = Fore.YELLOW + "W"
                gs.board[14][44] = Fore.YELLOW + "W"
                gs.board[14][45] = Fore.YELLOW + "W"
                gs.board[15][45] = Fore.YELLOW + "W"
                gs.building[15][44] = "WIZARD3"
                gs.building[14][44] = "WIZARD3"
                gs.building[14][45] = "WIZARD3"
                gs.building[15][45] = "WIZARD3"
            if no == 4:
                gs.board[35][41] = Fore.YELLOW + "W"
                gs.board[34][41] = Fore.YELLOW + "W"
                gs.board[34][40] = Fore.YELLOW + "W"
                gs.board[35][40] = Fore.YELLOW + "W"
                gs.building[35][41] = "WIZARD4"
                gs.building[34][41] = "WIZARD4"
                gs.building[34][40] = "WIZARD4"
                gs.building[35][40] = "WIZARD4"

        if color == "GREEN":
            if no == 1:
                gs.board[15][63] = Fore.GREEN + "W"
                gs.board[14][63] = Fore.GREEN + "W"
                gs.board[14][62] = Fore.GREEN + "W"
                gs.board[15][62] = Fore.GREEN + "W"
                gs.building[15][63] = "WIZARD1"
                gs.building[14][63] = "WIZARD1"
                gs.building[14][62] = "WIZARD1"
                gs.building[15][62] = "WIZARD1"
            if no == 2:
                gs.board[35][61] = Fore.GREEN + "W"
                gs.board[34][61] = Fore.GREEN + "W"
                gs.board[34][60] = Fore.GREEN + "W"
                gs.board[35][60] = Fore.GREEN + "W"
                gs.building[35][61] = "WIZARD2"
                gs.building[34][61] = "WIZARD2"
                gs.building[34][60] = "WIZARD2"
                gs.building[35][60] = "WIZARD2"
            if no == 3:
                gs.board[15][44] = Fore.GREEN + "W"
                gs.board[14][44] = Fore.GREEN + "W"
                gs.board[14][45] = Fore.GREEN + "W"
                gs.board[15][45] = Fore.GREEN + "W"
                gs.building[15][44] = "WIZARD3"
                gs.building[14][44] = "WIZARD3"
                gs.building[14][45] = "WIZARD3"
                gs.building[15][45] = "WIZARD3"
            if no == 4:
                gs.board[35][41] = Fore.GREEN + "W"
                gs.board[34][41] = Fore.GREEN + "W"
                gs.board[34][40] = Fore.GREEN + "W"
                gs.board[35][40] = Fore.GREEN + "W"
                gs.building[35][41] = "WIZARD4"
                gs.building[34][41] = "WIZARD4"
                gs.building[34][40] = "WIZARD4"
                gs.building[35][40] = "WIZARD4"

        if color == "RESET":
            if no == 1:
                gs.board[15][63] = " "
                gs.board[14][63] = " "
                gs.board[14][62] = " "
                gs.board[15][62] = " "
                gs.building[15][63] = " "
                gs.building[14][63] = " "
                gs.building[14][62] = " "
                gs.building[15][62] = " "
            if no == 2:
                gs.board[35][61] = " "
                gs.board[34][61] = " "
                gs.board[34][60] = " "
                gs.board[35][60] = " "
                gs.building[35][61] = " "
                gs.building[34][61] = " "
                gs.building[34][60] = " "
                gs.building[35][60] = " "
            if no == 3:
                gs.board[15][44] = " "
                gs.board[14][44] = " "
                gs.board[14][45] = " "
                gs.board[15][45] = " "
                gs.building[15][44] = " "
                gs.building[14][44] = " "
                gs.building[14][45] = " "
                gs.building[15][45] = " "
            if no == 4:
                gs.board[35][41] = " "
                gs.board[34][41] = " "
                gs.board[34][40] = " "
                gs.board[35][40] = " "
                gs.building[35][41] = " "
                gs.building[34][41] = " "
                gs.building[34][40] = " "
                gs.building[35][40] = " "
