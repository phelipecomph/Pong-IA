import random
from Game import Ball
class Player():
    def __init__(self, id):
        self.pos = 4
        self.spos = 4
        self.id = id
        self.points = 0
        self.board_size = 10
        self.board_cols = 58

    def action(self, ball, opponent):
        return self.simulate_sequence(ball)

    def simulate_sequence(self, ball):
        sequences = []
        points = []
        s_ball = {
            'x':ball.pos['x'],
            'y':ball.pos['y'],
            'horizontal':ball.direction['horizontal'],
            'vertical':ball.direction['vertical']
            }
        for i in range(10000):
            sequences.append([])
            points.append(0)
            i_ball = s_ball
            self.spos = self.pos
            for _ in range(15):
                i_ball, action, point = self.simulate(i_ball)
                sequences[-1].append(action)
                points[-1]+=point
                if action == -1: break
        # Ponderate actions
        action_points = {'w': 0, 's': 0,' ': 0}
        for i in range(len(sequences)):
            action_points[sequences[i][0]] += points[i]
        if action_points['w'] >= action_points['s'] and action_points['w'] >= action_points[' ']: return 'w'
        if action_points['s'] >= action_points['w'] and action_points['s'] >= action_points[' ']: return 's'
        if action_points[' '] >= action_points['s'] and action_points[' '] >= action_points['w']: return ' '

    
    def simulate(self, ball):
        action = random.choice(['w','s',' '])
        if action.lower() == 'w' and self.spos>=2:  self.spos -= 1
        if action.lower() == 's' and self.spos<=self.board_size-3: self.spos += 1
        if action.lower() == ' ': pass

        if ball['y'] == self.board_size-1 or ball['y'] == 1: ball['vertical'] = abs(ball['vertical']-1)
        if ball['vertical'] == 1: ball['y'] -= 1
        else: ball['y'] += 1
        
        if ball['x'] >= self.board_cols-5 and self.id == 1: 
            if self.pos+1 == ball['y']: ball['horizontal'] = abs(ball['horizontal']-1)
            return ball, action, -1

        if ball['x'] <= 4 and self.id == 0:
            if self.pos == ball['y']: ball['horizontal'] = abs(ball['horizontal']-1)
            return ball, action, -1

        if ball['x'] >= self.board_cols-5 and self.id == 0: 
            if self.pos+1 == ball['y']: ball['horizontal'] = abs(ball['horizontal']-1)
            return ball, action, 1

        if ball['x'] <= 4 and self.id == 1:
            if self.pos == ball['y']: ball['horizontal'] = abs(ball['horizontal']-1)
            return ball, action, 1
            
        if ball['horizontal'] == 1: ball['x'] += 1
        else: ball['x'] -= 1
        return ball, action, 0