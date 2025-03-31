import random



choice=int(input("What is Your choice?\n [Rock=0 or Paper=1 or Scissors=2]"))
computer_choice=random.randint(0,2)
print(choice,computer_choice)

if choice >2 or choice < 0:
        print("Invalid number buddy!")
elif choice==computer_choice:
        print("Its a draw")
elif choice==0 and computer_choice==2:
        print("You Win!")
elif choice==0 and computer_choice==1:
        print("Computer Wins!")
elif choice==1 and computer_choice==0:
        print("You win!")
elif choice==1 and computer_choice==2:
        print("Computer Wins!")
elif choice==2 and computer_choice==0:
        print("computer Win!")
elif choice==2 and computer_choice==1:
        print("you win")
    
