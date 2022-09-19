from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 

class model:
    #in the initial state we need to get to the corner
    #onece we are in the corner we need to loop in the hamilton cycle 
    def __init__(self):
        self.name='hamilton'
        self.in_cycle=False

    def get_snake_in_cycle(self, game):
        if(self.in_cycle):
            head = game.snake[0]
            snake_dir = game.snake[0] - game.snake[1]
            print(snake_dir)

class agent:
    def __init__(self):
        self.n_game = 0
        self.score=0

    def get_action():
        final_move = [0,0,0]
        move = random.randint(0,2)
        final_move[move]=1
        return final_move

def play():
    game = SnakeGameAI()
    mod=model()
    while True:
        # get move
        final_move = agent.get_action()
        #mod.get_snake_in_cycle(game)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)   

if(__name__=="__main__"):
    play()