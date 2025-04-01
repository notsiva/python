import random

# creating a function for getting the bet amount of the computer which is divisble by 100 for better calculation.
def computer_bet():
    computer_current_bet=random.randint(99, 1000)
    # print(computer_current_bet)
    if computer_current_bet%100!=0: #This condition whill check whether the random integer is divible by 100 and if the reminder is not zero it will restart the function again and again
        # print("if")
        return computer_bet()
    else:
        return computer_current_bet
    
users_total_bet=[]  # for updating the bet amount the user won
computers_total_bet=[] # for updating the bet amount the computer won



user_choice=int(input("Enter the bet Amount: $")) #for getting the user bet amount
computer_current_bet=computer_bet() # for starting the computer bet function to get the computer generated bet amount
print(f"The computer bets : ${computer_current_bet}")



choice=input("Do you wanna start the game? 'Y' or 'N' :\n").upper()
if choice=="Y":
    current_total_bet=(f"Total Bet amount: {user_choice+int(computer_current_bet)}")
    print(current_total_bet)
elif choice=="N":
    print("The game is terminated :X\n The bet amount cant be returned.")



