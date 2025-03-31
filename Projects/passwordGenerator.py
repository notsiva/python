import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','%','^','&','*','_']


# getting input 
no_letters=int(input("How many letters do you need in the Password:\n"))
no_numbers=int(input("How many numbers do you need in the Password:\n"))
no_symbols=int(input("How many Symbold do you need in the password:\n"))

# random_pass=[]

assign_letters=""
for random_symbols in letters:
    if len(assign_letters) < no_letters:
    #if len(asrandom_passsign_letters) < no_letters:    # for checking the length of the list
        assign_letters+=random.choice(letters)
        #assign_letters=random.choice(letters)
        #random_pass.append(assign_letters)     # this two lines are used for the adding the random letters to the list
assign_number=""
for random_numbers in numbers:
    if len(assign_number) <no_numbers:
         assign_number +=str(random.choice(numbers))
         
assign_symbols=""
for random_symbols in symbols:
    if len(assign_symbols) < no_symbols:
        assign_symbols+=random.choice(symbols)
        
print(assign_letters+assign_number+assign_symbols)
# print(random_pass)
    