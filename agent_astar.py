from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 
import numpy as np

class Agent:
    # Action
    # [1,0,0] -> Straight   -> 0 
    # [0,1,0] -> Right Turn -> 1
    # [0,0,1] -> Left Turn  -> 2

    def __init__(self):
        self.n_game = 0
        self.score=0

    def get_action(self, game):
        _head=game.head
        _food=game.food
        #all four nearest neighbour 
        right_neighbour = Point(_head.x+20,_head.y)
        left_neighbour = Point(_head.x-20,_head.y)
        up_neighbour = Point(_head.x,_head.y-20)
        down_neighbour = Point(_head.x,_head.y+20)

        right_distance = (right_neighbour,_food)
        left_distance = (left_neighbour,_food)
        up_distance = (up_neighbour,_food)
        down_distance = (down_neighbour,_food)

        distance_vec = np.array(right_distance, left_distance, up_distance, down_distance)
        print(distance_vec)
        print(np.argmin(distance_vec))


        move=1
        final_move = [0,0,0]
        final_move[move] = 1
        return final_move
    
    def manhattan(point1, point2):
        return abs(point1.x-point2.x) + abs(point1.y-point2.y) 

def play():
  
    agent = Agent()
    game  = SnakeGameAI()
   
    while True:
        final_move = agent.get_action(game) 
        reward, done, score = game.play_step(final_move) 
  
if(__name__=="__main__"):
    play()
