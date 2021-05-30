from Game import Game
from PlayerHuman import Player as HPlayer
from PlayerMonteCarlo import Player as MPlayer

if __name__ == '__main__':
    playerLeft = MPlayer(0)
    playerRight = MPlayer(1)
    game = Game(playerLeft,playerRight)
    game.show_board()
    
    while(game.gaming):
        game.turn()
        game.show_board()