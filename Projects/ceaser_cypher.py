alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction=input("Tye 'encode' for encrypting a message and 'decode' for decoding a message\n").lower()
# text=input("Type the word you wanna encrypt or decrypt\n")
# shift=int(input("Enter the shift number:\n"))
# print(alphabet.index("z"))



# while not decrypted:

def ceaser():
    while True:
        direction=input("Type 'encode' for encrypting a message and 'decode' for decoding a message\n").lower()
        
        if direction=="encode":
            text=input("Type the word you wanna encrypt\n")
            shift=int(input("Enter the shift number:\n"))
            
            def encrypt(text,shift):
                encrypted_text=""
                for letter in text:
                    if letter not in alphabet:
                        encrypted_text+=letter
                    else:
                        to_be_shifted=alphabet.index(letter) +shift
                        to_be_shifted%=len(alphabet)
                        encrypted_text+=alphabet[to_be_shifted]
                return encrypted_text   
            hidden_word=encrypt(text,shift)  
            print(hidden_word)     
             
                
               
        elif direction=="decode":
            text=input("Type the word you wanna decrypt\n")
            shift_back=int(input("Enter the decode number:\n"))
            def decrypt(text,shift_back):
                decrypted_text=""
                for i in text:
                    for letter in text:
                        if letter not in alphabet:
                            encrypted_text+=letter
                    else:
                        to_shift_back=alphabet.index(i)-shift_back
                        decrypted_text+=alphabet[to_shift_back]                   
                print(decrypted_text)
                
            decrypt(text=text,shift_back=shift_back)
        
        
        else:
            print("Please enter encode or decode")
            
            
            
        go_again=input("Do you wanna go again (y/n)\n")
        if go_again!='y':
            print("good bye")
            break
        else:
            ceaser()
        

ceaser()      
    


        