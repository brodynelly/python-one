def calculate_position(pos, vel, acc, t):
    result = pos + vel * t + 0.5 * acc * t**2
    return result

def get_non_negative_float_input(prompt):
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
    pos = get_non_negative_float_input("Initial position: ")
    vel = get_non_negative_float_input("Initial velocity: ")
    acc = get_non_negative_float_input("Acceleration: ")
    t = get_non_negative_float_input("Time: ")

    result = calculate_position(pos, vel, acc, t)
    print("Final position:", result)

    another_calculation = input("Do you want to calculate again? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Goodbye!")
        break
