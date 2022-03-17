import global_stuff as gs
class Spell: 
    def __init__(self):
        pass 
    def cast(self,inp):
        if inp == 'h':
            gs.KING_HEALTH *= 2
            gs.KING_HEALTH = min(gs.KING_HEALTH,1000)
        elif inp == 'r':
            gs.KING_ATTACK *= 2
            gs.KING_SPEED *= 2