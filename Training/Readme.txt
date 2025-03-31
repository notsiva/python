Code library 

1. Roller coster ride eligible if you are above a certain height using If and Else
        height=input("What is your height in cm: ")
        height_in_meters=round((int(height)/100),2)
        required_height=1.50
        if height_in_meters< required_height:
            print("You are not eligible for this ride lil bro 😂")
            
        else:
            print("Enjoy your ride big Guy 🫡")

2. What the fuck is this if statement 
            size_of_pizza=input('What size of pizza you need? (S,M, or L)\n')
            peperoni=input("Do you want pepperoni in your piza?(yes or no)\n")
            cheese=input("Do you want to add cheese? (Yes or No)\n")
            bill =0
            if size_of_pizza=="s":
                bill+=5
            elif size_of_pizza=="m":
                bill+=10
            elif size_of_pizza=="l":
                bill+=15
                
            if peperoni=="yes":
                    bill+=5
            if peperoni=="no":
                    bill
                    
            if cheese=="yes":
                        bill+=5
            if cheese=="no":
                        bill
            print(f"Your bill would be {bill}")

3.