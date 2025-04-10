import random
from instagram_celebreties import instagram_celebrities


# print(instagram_celebrities)

SCORE=0
game_over=False

choice=input("do you wanna start the game? 'Y' or 'N' :").upper()


def guessing(user_choice):
    global game_over
    if user_choice == "A":
        if instagram_celebrities[question1] > instagram_celebrities[question2]:
            print("You have won the game and the next question would be as follows")
            game_over=True
        else:
            print("pff You have lost the game!")
            game_over=True
    if user_choice == "B":
        if instagram_celebrities[question1] < instagram_celebrities[question2]:
            print("You have won the game and the next question would be as follows")
            game_over=True
        else:
            print("pff You have lost the game!")
            game_over=True

if choice=="Y":
    while not game_over:
        print("Try to guess the follower count of the two celebrities")
        question1=random.choice(list(instagram_celebrities))
        question2=random.choice(list(instagram_celebrities))
        print(f"{question1} \n {question2}")
        user_choices=input("Who has more followers? 'A' or 'B': \n")
        guessing(user_choice=user_choices)
else:
    game_over=True

        







