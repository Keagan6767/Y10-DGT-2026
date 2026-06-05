# Area and Perimeter Calculator
# Author: [Your Name]
# GitHub: [Your GitHub Link]

def get_positive_number(prompt):
    """Ask the user for a number greater than zero."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("That’s not a valid number. Try again.")

def calculate_area(width, height):
    """Calculate the area of a rectangle."""
    return width * height

def calculate_perimeter(width, height):
    """Calculate the perimeter of a rectangle."""
    return 2 * (width + height)

# Main program loop
while True:
    print("\n--- Area and Perimeter Calculator ---")
    width = get_positive_number("Enter the width: ")
    height = get_positive_number("Enter the height: ")

    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}")

    # Ask if user wants another calculation
    again = input("\nPress <Enter> to calculate again or any other key to quit: ")
    if again != "":
        print("Goodbye!")
        break
