# Demonstrate how variables are created and now the work
# Author: Keagan
# Date: 5/6/26 (M/D/Y)
# Version 1.1
# TODO:
#      Store a string
#      Store a different types of numbers
#      Assign the value of one variable to another
#      D0 calculations with variables and store the results

# Store a string 
greeting = "Hello world"
print(greeting)
random_variable = "7" # Storing a number as text
print(random_variable)

# Store different types of numbers
# Storing an integer (Whole Number)
num_1 = 7
print(f"The variable called num_1 which contrains {num_1} is a {type(num_1)}")

# Stores a float number(A nr with a decimal)
Num_2 = 9.5
print(f"The variable called num_1 is a {type(Num_2)}")

# assign the value of one variable to another
num_2 = greeting
print(f"num_2 has the value of {greeting}.")
print(f"Num_2 has now become a {type(num_2)}")

# Do calculations with variables and store the reslts
# Create a new/reassign variable
num_1 = 5
num_2 = 18

# Add up numbers
sum = 5 + 18
print(sum)