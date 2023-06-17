#is_raining = True
#is_cold = True
ask_rain = input("Is it raining? (Y/N): ")
ask_cold = input("Is it cold outside? (Y/N): ")

if ask_rain == "Y":
    is_raining = True
if ask_rain == "N":
    is_raining = False
else:
    print("Not a valid response, assuming its not raining!")
    is_raining = False

#ask_rain = input("Is it raining? (Y/N): ")
#ask_cold = input("Is it cold outside? (Y/N): ")

if ask_cold == "Y":
    is_cold = True
if ask_cold == "N":
    is_cold = False
else:
    print("Not a valid response, assuming its not raining or cold outsifr!")
    is_cold = False

print("\n\n")


if is_raining is True and is_cold is True:
    print("I will wear a hat and a scarf")
elif is_raining is True:
    print("I will wear a hat.")
elif is_cold is True:
    print("I will wear a scarf.")
else:
    print("Idont need to wear a hat or a scarf")