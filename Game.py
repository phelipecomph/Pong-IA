class Ball():
    def __init__(self,board):
        self.board_rows = len(board)
        self.board_cols = len(board[0])
        self.pos = {'x':round(self.board_cols/2),'y':round(self.board_rows/2)}
        self.direction = {'vertical':1,'horizontal':0} # [down/up,left/right] 
    
    def move(self,l_pos,r_pos):
        if self.pos['y'] == self.board_rows-1 or self.pos['y'] == 1: self.direction['vertical'] = abs(self.direction['vertical']-1)
        if self.direction['vertical'] == 1: self.pos['y'] -= 1
        else: self.pos['y'] += 1

        if self.pos['x'] == self.board_cols-5: 
            if r_pos+1 == self.pos['y']: self.direction['horizontal'] = abs(self.direction['horizontal']-1)
            else: return -1 #Point Left
        if self.pos['x'] == self.pos['x'] == 3:
            print('{0} {1}'.format(l_pos,self.pos))
            if l_pos+1 == self.pos['y']: self.direction['horizontal'] = abs(self.direction['horizontal']-1)
            else: return 1 #Point Right
            
        if self.direction['horizontal'] == 1: self.pos['x'] += 1
        else: self.pos['x'] -= 1
        return 0


class Game():
    def __init__(self,p1,p2):
        self.board = ['________________________________________________________  ',
                      '\                                                       / ',
                      '/                                                       \ ',
                      '\                                                       / ',
                      '/                                                       \ ',
                      '\                                                       / ',
                      '/                                                       \ ',
                      '\                                                       / ',
                      '/                                                       \ ',
                      '_________________________________________________________ ']

        self.ball = Ball(self.board)
        self.gaming = True
        self.p1 = p1
        self.p2 = p2
        

    def turn(self):
        action = self.p1.action(self.ball.pos)
        if action.lower() == 'w' and self.p1.pos>=2:  self.p1.pos -= 1
        if action.lower() == 's' and self.p1.pos<=len(self.board)-3:self.p1.pos += 1
        if action.lower() == ' ': pass
        ball_resposta = self.ball.move(self.p1.pos,self.p2.pos)
        if ball_resposta != 0:
            self.gaming = False

        action = self.p2.action(self.ball.pos)
        if action.lower() == 'w' and self.p2.pos>=2:  self.p2.pos -= 1
        if action.lower() == 's' and self.p2.pos<=len(self.board)-3:self.p2.pos += 1
        if action.lower() == ' ': pass
        ball_resposta = self.ball.move(self.p1.pos,self.p2.pos)
        if ball_resposta != 0:
            self.gaming = False

    
    def show_board(self):
        for _ in range(10): print()
        for b in range(len(self.board)):
            row = self.board[b] 
            if self.p1.pos == b: row = row[:2] + '|' + row[3:]
            if self.p2.pos == b: row = row[:-4] + '|' + row[-3:]
            if self.ball.pos['y'] == b: row = row[:self.ball.pos['x']] + 'o' + row[self.ball.pos['x']+1:]
            print(row)

if __name__ == '__main__':
    game = Game()
    game.show_board()
    while(game.gaming):
        game.play()
        game.show_board()