import random
def dice(response):
    while response == "y":
        no=random.radint(1,6)
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            print(response)
response=input("press y to roll again and n to exit")    
dice(int(response))






