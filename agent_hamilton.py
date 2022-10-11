from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 
import numpy as np

def model_hamilton():
    dir_map=np.load('direction_map.npy')
    #dir_map = np.load('direction_map2.npy')
    
    map = np.zeros((32,24))
    #First path 
    map[:,22]= 1
    map[0,22]= 0
    map[31,22]=0
    map[:,0] = 2
    map[0,23]= 2
    map[31,23]= 2
    map[30,0]= 2

    #Second path¨

    # map[0,:] = 2
    # map[15,:] = 1
    # map[15,0]=0
    # map[15,23] = 0
    # map[31,:] = 2

    # map[16,:] = 1
    # map[16,23]=0
    # map[16,0] = 0

    # print(map[15,:])
    
    # print(map)
 
    return map , dir_map

class Agent:
    # Action
    # [1,0,0] -> Straight   -> 0 
    # [0,1,0] -> Right Turn -> 1
    # [0,0,1] -> Left Turn  -> 2

    def __init__(self, in_map, in_dir_map=0):
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
            print(head.x, head.y)
            move = int(self.map[int((head.x/20)), int((head.y/20))])# 32 x 24 -> 31 x 23
            print('acc to map')
        else:
            move=np.random.randint(3)
            print('random')

        final_move = [0,0,0]
        final_move[move] = 1
        return final_move

def play():
    map, dir_map= model_hamilton()
    #map = model_hamilton()
    #agent = Agent(map)
    agent = Agent(map, dir_map)
    game  = SnakeGameAI()
   
    while True:
        final_move = agent.get_action(game) 
        done, score, _, _,_ = game.play_step(final_move) 
  
if(__name__=="__main__"):
    play()

    