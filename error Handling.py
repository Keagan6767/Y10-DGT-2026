# Create and error handling function
# Author: Keagan Hockly
# Date: 08 May 2026
# Version 3

'''# Code that tests that a valid number is entered (V1)
done = False # Boolean variable set to False
# While loop that runs until a valid nr is entered
while not done:
    num = int(input("Please enter your number: "))
    done = True
   
print(f"The number you entered is {num}.")'''

# Code that tests that a valid number is entered (V2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that does something.
# I can use a function over and over. To use a function
# I 'call' it by writing out its name.
'''def test_int_num():
    done = False
    while not done:
        try: # This tries for a valid input
            num = int(input("Please enter your number: "))
            done = True
           
        except ValueError:
            print("That is not a vlaid integer.")
           
    return(num)
   
# Main routine
num_1 = test_int_num()
print(f"You entered {num_1} as your first number.")

num_2 = test_int_num()
print(f"You entered {num_2} as your second number.")
print() # One way of creating a line break.
sum = num_1 + num_2 
print(f"Your two Numbers added together are {sum}")

multiply = num_1 * num_2 
print(f"The numbers multiplied together with eachother results is {multiply}")

#Division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to {divide}.")'''

# Version 3. Refining my code. Making it more pythonic.
# This will result in being able to change the question in the function.
def test_int_num(question, low, high): # 'question' is a place holder.
    done = False
    error = f"Whoops, that is not an integer between {low} and {high}."
    while not done:
        # print(question)
        try: # tries vaid input
            num = int(input(question))
            if num >= low and num <= high:
                done = True
            
            else:
                print(error)
                print()

        except ValueError:
            print("error")

    return(num)

# Main Routine
num_1 = test_int_num("Please enter a number between 1 and 10: ", 1, 10)
print(f"You entered {num_1}.\n")

num_2 =  test_int_num ("Please enter a number between 15 and 25:", 15, 25)
print(f"You entered {num_2}.\n")

num_3  = test_int_num("Please enter a number between 30 and 40: ", 30,40)
print(f"You entered {num_3}.\n")

sum = num_1 + num_2 + num_2
print(f"Your two Numbers added together are {sum}")

multiply = num_1 * num_2 * num_3
print(f"The numbers multiplied together with eachother results is {multiply}")

#Division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to {divide}.")