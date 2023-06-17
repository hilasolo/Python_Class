import random

target_number = random.randint(1, 100)
guessed_corretly = False

while not guessed_corretly:
    user_input = int(input("Guess a number between 1 to 100: "))

    if user_input < target_number:
        print("Higher!")
    elif user_input > target_number:
        print("Lower!")
    else: 
        print("amazing! you have found the number")
        guessed_corretly = True
