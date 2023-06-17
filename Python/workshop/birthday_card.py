#take input from user
name = (input("Please enter you name: "))
sender = "Hilariano"
year_of_birth = int(input("Please enter your year of birth: "))

#Current year: set current year = to 2023 
current_year = 2023

#calculate the age of the recipient based on the current year and the year of birth provided.
Age = current_year - year_of_birth

#Generate a personalized birthday card 
print (f"{name} let's celebrate your {Age} years of awesomeness! Wishing you a day filled with joy and laughter as you turn {Age}!.")
print (f"With love and best wishes.\n {sender} ")
