def calculate_position(pos, vel, acc, t):
    result = pos + vel * t + 0.5 * acc * t**2
    return result

def check_valid(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Oops! Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

while True:
    pos = check_valid("Initial position: ")
    vel = check_valid("Initial velocity: ")
    acc = check_valid("Acceleration: ")
    t = check_valid("Time: ")

    result = calculate_position(pos, vel, acc, t)
    print("Final position:", result)

    another_calculation = input("Do you want to calculate again? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Goodbye!")
        break
