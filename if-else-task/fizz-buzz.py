num = int(input("enter a number : "))
i = 0
while num != i:
    i+=1
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)