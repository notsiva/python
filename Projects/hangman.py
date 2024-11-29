import random


random_words=["sivakaran","manokaran","sasikaran","suriyaSekar","muppudathi"]
stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(stages[0])
length_of_list=len(random_words)

#Generating random word from the above list
random_word_generated=random.choice(random_words)
# print(random_word_generated)


#creating a place holder for this word
placeholder=""
for i in random_word_generated:
    placeholder+="_"
print("Find this random Word!")
print(placeholder)


#Getting input from the user
at_goal=False
correct_letters=[]
life=7
#replacing the letter user choosed with the place holder
while not at_goal:
    letter_guess=input("Which letter you are choosing?\n").lower()
    print(letter_guess)
    guess=""
    for i in random_word_generated:
        if i==letter_guess:
            guess+=i
            correct_letters.append(i)
        elif i in correct_letters:
            guess+=i
            
            
        else:
            guess+="_"
    if letter_guess not in (random_word_generated): 
        life-=1
        
        print(stages[-(life)])
        print(f"you got {life} lives left!")
        if life==0:
            at_goal=True
            print("Game Over")
        
     
            
    print(guess)
    if "_" not in guess:
        at_goal=True
        print("You won my guy!")