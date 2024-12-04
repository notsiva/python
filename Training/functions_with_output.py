first_name=input("What is your first name?\n")
last_name=input("What is your last name\n")

def title_case(first_name,second_name):
    """This will print the first and last name as concatenate"""
    full_name=first_name.title()+" "+second_name.title()
    return full_name

name=title_case(first_name,last_name)
print(name)

# year=int(input("Enter the year for checking it is leap year or not: "))
# def is_leap_year(year):
#     # Write your code here. 
#     # Don't change the function name.
#     if year%4==0:       
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:           
#                 return False
#         else:   
#             return True
#     else:
#         return False    
        
# print(is_leap_year(2024))