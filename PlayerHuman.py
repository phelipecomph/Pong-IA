class Player():
    def __init__(self, id):
        self.pos = 4
        self.id = id
        self.points = 0

    def action(self, ball, opponent):
        return input() # 'w': up 's': down ' ': stay