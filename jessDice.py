import random

player = random.randint (1,6) #variable
ai = random.randint(1,6) #variable

def dice():

    #DICE ROLL
    print("You rolled " + str(player))
    print("AI rolled" + str(ai))

    #DICE CHECK
    if player > ai:
        print("Win!")
    elif player == ai:
        print("Tie")
    else:
        print("Lose")

#REPLAY
while True:
    print("Press return to roll again")
    roll = input
    dice()


    

    

