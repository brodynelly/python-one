#run the prgram again 
running_program = True

#sort array integers 
def sort_array_integers(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#median of the numbers
def median(array):
    sorted_array = sort_array_integers(array)
    if len(sorted_array) % 2 == 0:
        return (sorted_array[len(sorted_array) // 2 - 1] + sorted_array[len(sorted_array) // 2]) / 2
    else:
        return sorted_array[len(sorted_array) // 2]

#mode of numbers using dictionary notation
def mode(number_list):
    number_counts = {}
    for number in number_list:
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    #determin the mode numbers
    max_count = max(number_counts.values())
    mode_numbers = []
    for num, count in number_counts.items():
        if count == max_count:
            mode_numbers.append(num)
    return mode_numbers
    
 
while running_program:
    
    #open file with test error
    try:
        # Accept an input from the user for the file name
        fileName = input("Enter file name: ")

        # Open the file with error handling
        with open(fileName) as f:
            # Print the file name
            print("File name:", fileName)       

            # Add integers from the file to a list
            integers = []
            for line in f.readlines():
                line = line.strip()
                try:
                    integer_value = int(line)
                    integers.append(integer_value)
                except ValueError:
                    print(f"Invalid input: '{line}' is not a valid positive integer.")
                    continue

            if len(integers) == 0:
                raise ValueError
            
    except FileNotFoundError:
        print("File not found. Please try again.")
        continue
    except ValueError: 
        print("text file {fileName} is empty. Please try again.")
        continue

    #sum the list
    total = sum(integers)
    print(f"Sum: ", total)

    #count number of elements in list
    print(f"Count: ", len(integers))

    #sort the list
    print(f"average: ", sum(integers) / len(integers))

    #maximum element in list
    print(f"Max: ", max(integers))

    #minimum element in list
    print(f"Min: ", min(integers))

    #range of elements in list
    print(f"Range: ", max(integers) - min(integers))

    #median of the numbers 
    print(f"Median: ", median(integers))

    #mode of the numbers
    print(f"Mode: ", mode(integers))

    #ask user to continue or quit program, ask again if they don't input correct values
    
    continue_program = input("Would you like to evaluate another file? (y/n)").lower()
    if continue_program != 'y':
        f.close
        running_program = False
        break

    #close file
    f.close()







