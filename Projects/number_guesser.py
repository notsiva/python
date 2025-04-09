import random

random_number=random.randint(1,100)  #the computer think of a random number and store it in the variabel for the user to guess
print(random_number)

choice=input("Enter the dificulty level - 'Easy' or 'Hard' : ").upper() # for the level choosing
print(choice)

guess=0
if choice=="EASY":
    guess=10
    game_over=False
    while not game_over:
        print(f"You only have {guess} guess to identify the correct number:")
        user_guess=int(input("Enter the number: "))
        
        if guess==0:
            print("Game Over")
            game_over=True
            break
        if user_guess==random_number:
            print(f"You have won the game and the correct number is {user_guess}")
            game_over=True
        
        elif user_guess>random_number:
                print("Too High")
        elif user_guess<random_number:
            print("Too Low")
        guess-=1

if choice=="HARD":
    guess=5
    game_over=False
    while not game_over:
        print(f"You only have {guess} guess to identify the correct number:")
        user_guess=int(input("Enter the number: "))
        if guess==0:
            print("Game Over")
            game_over=True
            break
        if user_guess==random_number:
            print(f"You have won the game and the correct number is {user_guess}")
            game_over=True
        elif user_guess>random_number:
                print("Too High")
        elif user_guess<random_number:
            print("Too Low")
        guess-=1





