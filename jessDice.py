import random
import time

player = random.randint (1,6) #variable
ai = random.randint(1,6) #variable

def dice(): #FUNCTION

    #DICE ROLL
    print("You rolled " + str(player))
    time.sleep(3)
    print("The computer rolled " + str(ai))
    time.sleep(3)
    
    #DICE CHECK
    if player > ai:
        print("Win!")
    elif player == ai:
        print("Tie")
    else:
        print("Lose")
    time.sleep(3)

#REPLAY
while True:
    print("Press return to roll")
    roll = input
    dice()


    

    

