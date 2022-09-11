import random
response="y"
while response =="y":
    n=random.randint(1,6)
    response=input("Press y to play the game and n to end")
    if n == 1:
        print("---0---")
    if n ==2:
        print("---00---")
    if n==3:
        print("---000---")
    if n ==4 :
        print("---0000---")
    if n ==5:
        print("---00000---")
    if n ==6:
        print("---000000---")
    
    





