number = int(input("Enter a number"))
x = number // 2
while x> 1:
    if number % x == 0:
        print(f"{number} has factor {x}")
    x -= 1