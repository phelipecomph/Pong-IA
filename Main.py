from Game import Game
from PlayerHuman import Player

if __name__ == '__main__':
    playerLeft = Player()
    playerRight = Player()
    game = Game(playerLeft,playerRight)
    game.show_board()
    
    while(game.gaming):
        game.turn()
        game.show_board()