import math

def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive number.")

def calculate_gallons_and_labor(square_feet):
    gallons_of_paint = math.ceil(square_feet / 350)
    hours_of_labor = square_feet / 350 * 6
    return gallons_of_paint, hours_of_labor

def main():
    print("Welcome to the Paint Job Estimator!")

    while True:
        square_feet = get_positive_float_input("Enter the square feet of wall space to be painted: ")
        price_per_gallon = get_positive_float_input("Enter the price of the paint per gallon: $")

        gallons_of_paint, hours_of_labor = calculate_gallons_and_labor(square_feet)
        total_paint_cost = gallons_of_paint * price_per_gallon
        labor_charges = hours_of_labor * 62.25
        total_cost = total_paint_cost + labor_charges

        print("\nEstimation Results:")
        print(f"Number of gallons of paint required: {gallons_of_paint}")
        print(f"Hours of labor required: {hours_of_labor:.1f} hours")
        print(f"Cost of the paint: ${total_paint_cost:.2f}")
        print(f"Labor charges: ${labor_charges:.2f}")
        print(f"Total cost of the paint job: ${total_cost:.2f}")

        another_estimate = input("Would you like to do another estimate? (y/n): ").lower()
        if another_estimate != 'y':
            print("Thank you for using the Paint Job Estimator!")
            break

if __name__ == "__main__":
    main()
