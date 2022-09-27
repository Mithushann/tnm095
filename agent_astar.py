from decimal import MIN_EMIN
from environment import SnakeGameAI,Direction,Point,BLOCK_SIZE
import random 
import numpy as np

class Agent:
    # Action
    # [1,0,0] -> Straight   -> 0 
    # [0,1,0] -> Right Turn -> 1
    # [0,0,1] -> Left Turn  -> 2

    #Orientation
    # 1 -> right -> ( 20 ,   0)
    # 2 -> left  -> (-20 ,   0)
    # 3 -> up    -> (  0 , -20)
    # 4 -> down  -> (  0 ,  20)


    def __init__(self):
        self.n_game = 0
        self.score=0
    
    def is_hinderence(self,in_snake, box):
        for _box in in_snake:
            if _box.x==box.x and _box.y==box.y:
                return True
        return False

    def get_action(self, game):
        _head  = game.head
        _food  = game.food
        _snake = game.snake

        #all four nearest neighbour 
        right_neighbour = Point(_head.x+20,_head.y)
        left_neighbour  = Point(_head.x-20,_head.y)
        up_neighbour    = Point(_head.x,_head.y-20)
        down_neighbour  = Point(_head.x,_head.y+20)

        # Calculating the distance between future location of the head and food 
        if self.is_hinderence(_snake,right_neighbour):
            right_distance=9999
        else:
            right_distance = self.manhattan(right_neighbour,_food)
        
        if self.is_hinderence(_snake,left_neighbour):
            left_distance=9999
        else:
            left_distance  = self.manhattan(left_neighbour,_food)

        if self.is_hinderence(_snake,up_neighbour):
            up_distance=9999
        else:
            up_distance    = self.manhattan(up_neighbour,_food)

        if self.is_hinderence(_snake, down_neighbour):
            down_distance=9999
        else:
            down_distance  = self.manhattan(down_neighbour,_food)

        distance_vec = np.array([right_distance, left_distance, up_distance, down_distance])
         
        # What action should we take to go to closest neighbour
    
        direction_cns = np.array([])
        for dist in distance_vec:
            min_index     = np.argmin(distance_vec) 
            direction_cns = np.append(direction_cns, min_index)
            distance_vec[min_index]=10000 #inf
            
        for i,dir_cn in enumerate(direction_cns):
            dir_cn=int(dir_cn+1)
            #The direction of snake and the direction we travel is oposit to each others 
            if(i==0 and dir_cn==1 and game.direction==Direction.LEFT or dir_cn==2 and game.direction==Direction.RIGHT
             or dir_cn==3 and game.direction==Direction.DOWN or dir_cn==4 and game.direction==Direction.UP):
                move = random.randint(1,2)
                break

            # current snake direction right
            elif(game.direction==Direction.RIGHT):
                move='right'
                #turn left
                if (dir_cn==3):
                    move=2; break
                #turn right
                elif(dir_cn==4):
                    move=1; break
                #continue to go straigt 
                elif(dir_cn==1):
                    move=0; break
            
            # current snake direction left 
            elif (game.direction==Direction.LEFT):
                move='left'
                #turn right
                if (dir_cn==3):
                    move=1; break
                #turn left
                elif(dir_cn==4):
                    move=2; break
                #continue to go straigt 
                elif(dir_cn==2):
                    move=0; break

            elif (game.direction==Direction.UP):
                #turn left
                move='up'
                if (dir_cn==2):
                    move=2; break
                #turn right
                elif(dir_cn==1):
                    move=1; break
                #continue to go straigt 
                elif(dir_cn==3):
                    move=0; break

            # current snake direction down
            elif (game.direction==Direction.DOWN):
                move='down'
                #turn left
                if (dir_cn==1):
                    move=2; break
                #turn right
                elif(dir_cn==2):
                    move=1; break
                #continue to go straigt 
                elif(dir_cn==4):
                    move=0; break
            else:
                move=0
                print('Something is breaking')
        
        final_move = [0,0,0]
        final_move[move] = 1
        return final_move
    
    def manhattan(self, point1, point2):
        return int(abs(point1.x-point2.x) + abs(point1.y-point2.y)) 

def play():
  
    agent = Agent()
    game  = SnakeGameAI()
    sum=0
    high_score=0
    while True:
        final_move = agent.get_action(game) 
        reward, done, score = game.play_step(final_move) 
        if done:
            game.reset()
            agent.n_game += 1
            sum = sum +score
            avg = int(sum/agent.n_game)

            if score > high_score:
                high_score=score

            print('Game: ',agent.n_game,'Score: ',score, 'Average: ',avg, 'Record: ',high_score)
        if agent.n_game>=100:
            break
  
if(__name__=="__main__"):
    play()
