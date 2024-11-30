alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction=input("Tye 'encode' for encrypting a message and 'decode' for decoding a message\n").lower()
# text=input("Type the word you wanna encrypt or decrypt\n")
# shift=int(input("Enter the shift number:\n"))
# print(alphabet.index("z"))

decrypted=False

# while not decrypted:
while not decrypted:
    def ceaser():
        direction=input("Type 'encode' for encrypting a message and 'decode' for decoding a message\n").lower()
        hidden_word=""
        if direction=="encode":
            text=input("Type the word you wanna encrypt\n")
            shift=int(input("Enter the shift number:\n"))
            
            def encrypt(text,shift):
                encrypted_text=""
                for letter in text:
                    to_be_shifted=alphabet.index(letter) +shift
                    to_be_shifted%=len(alphabet)
                    encrypted_text+=alphabet[to_be_shifted]
                    
                    
                print(encrypted_text)  
            hidden_word=encrypt(text,shift)
            go_again=input("Do you wanna go again (y/n)\n")
            if go_again=='y':
                ceaser()
            else:
                decrypted=True
                        


                
        elif direction=="decode":
            shift_back=int(input("Enter the decode number:\n"))
            def decrypt(hidden_text,shift_back):
                decrypted_text=""
                for i in hidden_text:
                    to_shift_back=alphabet.index(i)-shift_back
                    decrypted_text+=alphabet[to_shift_back]

                    
                print(decrypted_text)
            decrypt(hidden_word,shift_back)
            go_again=input("Do you wanna go again (y/n)\n")
            if go_again=='y':
                ceaser()
            else:
                decrypted=True

    ceaser()      
    


        