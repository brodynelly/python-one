#run the prgram again 
running_program = True
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
    except FileNotFoundError:
        print("File not found. Please try again.")
        continue

    #sum the list
    total = sum(integers)
    print(f"Sum: ", total)

    #count number of elements in list
    print("Count: ", len(integers))

    #sort the list
    print("average: ", sum(integers) / len(integers))

    #maximum element in list
    print("Max: ", max(integers))

    #minimum element in list
    print("Min: ", min(integers))

    #range of elements in list
    print("Range: ", max(integers) - min(integers))

    #ask user to continue or quit program, ask again if they don't input correct values
    
    continue_program = input("Would you like to evaluate another file? (y/n)").lower()
    if continue_program != 'y':
        f.close
        running_program = False
        break

    #close file
    f.close()







