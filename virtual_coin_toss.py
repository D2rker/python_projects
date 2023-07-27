import random

should_end = False
while not should_end:
    random_side = random.randint(0,1)
    if random_side == 1:
        print("head")
    else:
        print("tails")

    restart = input("type 'yes' if you want to continue:  ")
    if restart == "no":
        should_end = True
        print("good bye")
