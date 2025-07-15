import random

def game():
    print("You are playing the game...")
    score = random.randint(1,99)
    #fetch the highscore
    with open("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore=0

    print(f"your score : {score}")
    if(score>highscore):
        #write this highscore in to the file
        with open ("highscore.txt","w") as f:
            f.write(str(score))  #f.string takes argument as string

    return score

game()                    