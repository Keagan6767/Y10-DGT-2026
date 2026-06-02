# Fencing Cost Calculator
# Author: Keagan Hockly
# Date: 5/27/26
# version 1

print("Welcome to the Fencing Cost Calculator!")

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a proper number.")

while True:
    # Ask the user for inputs with validation
    length = get_number("Enter the length of the area (m): ")
    width = get_number("Enter the width of the area (m): ")
    cost_per_m = get_number("Enter the cost of fencing per metre: ")

    # Calculate perimeter
    perimeter = 2 * (length + width)

    # Calculate total cost
    total_cost = perimeter * cost_per_m

    # Display result
    print(f"\nThe perimeter is {perimeter} m.")
    print(f"The total cost of fencing is ${total_cost:.2f}\n")

    # Ask if they want another calculation
    again = input("Do you want to do another calculation? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for using the Fencing Cost Calculator!")
        break
