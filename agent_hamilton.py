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
        self.in_cycle=False

    def get_action(self, game):
        head = game.snake[0]
        x = game.snake[0].x - game.snake[1].x
        y = game.snake[0].y - game.snake[1].y
        snake_dir=[ x , y ]

        final_move = [0,0,0]

        #before getting inside the cycle
        if (self.in_cycle is False):
            move = self.get_snake_in_cycle(game)

        #at x position 0 and direction left 
        elif head.x == 0.0 and np.array_equal(snake_dir, [-20.0, 0.0] ):
            print(head)
            print(snake_dir)
            move=1
            self.in_cycle=True
        
        #at all four corners
        elif  (np.array_equal(head,[0,0]) and np.array_equal(snake_dir,[0.0, -20.0])  or
        np.array_equal(head,[640,480]) or 
        np.array_equal(head,[640,0]) or 
        np.array_equal(head,[0,480])):
            move=1
            print('head')

        final_move[move] = 1
        return final_move


    #in the initial state we need to get to the corner
    #onece we are in the corner we need to loop in the hamilton cycle 
    def get_snake_in_cycle(self, game):
        head = game.snake[0]
       
        x = game.snake[0].x - game.snake[1].x
        y = game.snake[0].y - game.snake[1].y
        snake_dir=[ x , y ]
        if np.array_equal(snake_dir,[20.0, 0.0]):   
            if head.y > 240:
                #turn left
                mv = 2
            else:
                #trun right
                mv = 1
        if np.array_equal(snake_dir,[0.0, 20.0]):
            #print('down')
            mv= 1
        if np.array_equal(snake_dir,[0.0, -20.0]):
            #print('upp')
            mv= 2
        if np.array_equal(snake_dir,[-20.0, 0.0]):
            #print('left')
            mv= 0
        return mv
       

def play():
    agent = Agent()
    game  = SnakeGameAI()
    
    while True:
        # get move
        final_move = agent.get_action(game)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)   

if(__name__=="__main__"):
    play()