import random
from game_logic import GameLogic


class Game() :  
    def play(self):
        player = GameLogic()
        player.play_game()



            
if __name__ == "__main__":
    new_game = Game()
    new_game.play()