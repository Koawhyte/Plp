def calculator():
        
   
#Getting the user input for the two numbers and the operation#

        num1 = float(input ("Please Enter your first Number :"))
        operation = input("Enter the Operation(+, -, *, /):")
        num2 = float(input ("Please Enter your second Number :"))

        #Performing the operation based on the users input
        if operation == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")

        elif operation == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")

        elif operation == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")

        elif operation == '/':
                if num2 !=0:
                   result = num1 / num2
                   print(f"{num1} / {num2} = {result}")
                else:
                   print("Error: Division by Zero is not allowed. ")
        else:
                print("Error: Invalid operation. please use +, -, * or /  ")

calculator()