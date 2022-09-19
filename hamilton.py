from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 

class agent:
       def __init__(self):
        self.n_game = 0
        self.score=0

        def get_action(self):
 
            final_move = [0,0,0]

            move = random.randint(0,2)
            final_move[move]=1

            return final_move

def play():
    game = SnakeGameAI()
    while True:
        # get move
        final_move = agent.get_action()

        # perform move and get new state
        reward, done, score = game.play_step(final_move)   

if(__name__=="__main__"):
    play()