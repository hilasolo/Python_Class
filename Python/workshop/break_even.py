import math
#take input from user

#fixed_cost (float): the fixed cost of the product
fixed_cost = float(input("Enter fixed costs: "))

#variable_cost (float): the variable cost per unit of the product
variable_cost = float(input("Enter variable cost per unit: "))

#price(float): the selling price per unit of the product
price = float(input("Enter selling price per unit: "))

#calcu;ate the the break even point: fixed_cost / (price - variable_cost)
break_even_point = fixed_cost / (price - variable_cost)

#print the result
print (f"The break-even point is at {break_even_point} units.")
print (f"The break-even point is at {break_even_point:.2f} units.")
print (f"The break-even point is at {int(break_even_point)+1} units.")
print (f"The break-even point is at {math.ceil(break_even_point)} units.")
print (f"The break-even point is at {math.floor(break_even_point)} units.")
print (f"The break-even point is at {round(break_even_point)} units.")

