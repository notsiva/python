import random


def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value, max_value)
    
    return roll
while True:
    PlayerCount=input("Enter the number of Players(2-4): ")
    if PlayerCount.isdigit():
        PlayerCount=int(PlayerCount)
        if 2 <= PlayerCount <= 4:
            break
        else:
            print("Enter a number between 2 to 4")
    else:
        print("Invalid Input, try Agin")
        
max_socre=50
player_score=[0 for _ in range(PlayerCount)]

        
        
    