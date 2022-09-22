from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 
import numpy as np

def model_hamilton():
    dir_map=np.load('direction_map.npy')
    map = np.zeros((32,24))
    map[:,22]= 1
    map[0,22]= 0
    map[31,22]=0
    map[:,0] = 2
    map[0,23]= 2
    map[31,23]= 2
    map[30,0]= 2
 
    return map, dir_map

class Agent:
    # Action
    # [1,0,0] -> Straight   -> 0 
    # [0,1,0] -> Right Turn -> 1
    # [0,0,1] -> Left Turn  -> 2

    def __init__(self, in_map, in_dir_map):
        self.n_game = 0
        self.score=0
        self.in_cycle=False
        self.map = in_map
        self.dir_map=in_dir_map

    def get_action(self, game):
        head = game.snake[0]
        dir=0
        if game.direction == Direction.RIGHT:
            dir=1
        elif game.direction == Direction.LEFT:
            dir=2
        elif game.direction == Direction.UP:
            dir=3
        elif game.direction == Direction.DOWN:
            dir=4
        
        if(dir==self.dir_map[int((head.x/20)), int((head.y/20))]):
            move = int(self.map[int((head.x/20)), int((head.y/20))])
            print('acc to map')
        else:
            move=np.random.randint(3)
            print('random')

        final_move = [0,0,0]
        final_move[move] = 1
        return final_move

def play():
    map, dir_map= model_hamilton()
    agent = Agent(map, dir_map)
    game  = SnakeGameAI()
   
    while True:
        final_move = agent.get_action(game) 
        reward, done, score = game.play_step(final_move) 
  
if(__name__=="__main__"):
    play()

    