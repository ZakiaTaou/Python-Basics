for i in range(4):
    year = int(input("enter year : "))
    if year % 4 == 0 or year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 != 0 :
        print(f"{year} is not a leap year")