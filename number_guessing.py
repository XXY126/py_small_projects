import random

range = int(input("INSERIRE RANGE\n"))
flag = 0
random.seed()
rand = random.randint(0, range)

while flag == 0:
    guess = int(input("INDOVINA IL NUMERO!\n"))
    if(guess>rand):
        print('LOWER')
    else:
        if(guess<rand):
            print('HIGHER')
        else:
            print("INDOVINATO")
            flag=1;

print("il numero era ", rand)