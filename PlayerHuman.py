class Player():
    def __init__(self):
        self.pos = 4
        self.points = 0

    def action(self, ball):
        return input() # 'w': up 's': down ' ': stay