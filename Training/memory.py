operations=["+","-","*","/"]
should_accumulate=True

while should_accumulate:
    number1=int(input("What is the first number? : \n"))
    for i in operations:
        print(i)
    operation=input("What is the operation you need to done? : ")
    number2=int(input("What is the second number? : \n"))
    

    def calculater(firstNumber=number1,secondNumber=number2):
        result=0
        if operation=="add":
            result=number1+number2
        elif operation=="sub":
            result=number1-number2
        elif operation=="mult":
            result=number1*number2
        elif operation=="div":
            result=number1/number2
        print(result)

    calculater(number1,number2)
    final_answer=calculater(number1,number2)

    choice=input("Should you continue with the current number or create a new calculation? : ")
    if choice=="y":
        number1=final_answer
    else:
        should_accumulate=False



