while True:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operator (+,-,*,/,**): ")
    num2 = float(input("Enter second number: "))
    if operation == "+":
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == "-":
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operation == "*":
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operation == "/":
        if num2 == 0:
            print("dividing By 0 is not possible ")
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
    elif operation == "**":
        print(f'{num1} ** {num2} = {num1 ** num2}')
