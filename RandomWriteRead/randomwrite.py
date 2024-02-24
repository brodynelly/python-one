import random

while True: 
    try: 
        #ask user for possitive upper and lower bounds 
        number_of_elements = int(input("Enter the number of elements: "))
        upper_bound = int(input("Enter the upper bound: "))
        lower_bound = int(input("Enter the lower bound: "))
        
        #continues the loop if the possitive upper bound is less than the possitive lower bound but terminates the loop if the upper bound is greater than the lower bound 
        if upper_bound < lower_bound and upper_bound > 0 and lower_bound > 0 and number_of_elements > 0:
            print("Oops! The upper bound must be greater than the lower bound and both entities to be positive. Try again.")
        else:

            #file already exist 
            try: 
                with open("randomnum.txt", "w") as f:
                    for i in range(number_of_elements):
                        random_number = random.randint(lower_bound, upper_bound)
                        f.write(str(random_number) + "\n")
                
            #file does not exist 
            except FileNotFoundError:
                with open("randomnum.txt", "a") as f:
                    for i in range(number_of_elements):
                        random_number = random.randint(lower_bound, upper_bound)
                        f.write(str(random_number) + "\n")

            break
    except ValueError:
        print("Oops! That's not a valid number. Try again.")
 
#validate that the file exists and that the file is not empty 
print("File randomnum.txt created.")

#close the file
f.close()                                                    

