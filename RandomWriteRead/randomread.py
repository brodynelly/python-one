

#open file with test error
try: 
    with open("randomnum.txt") as f:
        #display numbers line by line from file 
        print(f"list of random numbers in randomnum.txt:")

        #print each line of random numbers
        count = 0
        for line in f:
            print(line)
            count = count + 1

        #count number of elements in list
        print(f"random number count: {count}")

    #close file
    f.close()

except FileNotFoundError:
    print("File not found. Please try again.")
