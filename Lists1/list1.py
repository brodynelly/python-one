#prints the different by iterating over the changed list from the parameter
def display_list(items):
    for item in items:
        print(item)

#create the original list and display it
foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"]

# Display the original list
print("foods in original order:")
display_list(foods)

#sort the original list in ascending alphabetical order and display it
foods.sort()
print("foods in ascending alphabetical order:")
display_list(foods)

#sort the original list in descending alphabetical order
foods.sort(reverse=True)
print("foods in descending alphabetical order:")
display_list(foods)

# Create a sorted copy of the foods list
foods2 = sorted(foods)
print("foods2 in ascending alphabetical order:")
display_list(foods2)

#display the original list to show it remains unchanged
print("foods still in descending alphabetical order:")
display_list(foods)

#reverse the order of items in the original list
foods.reverse()
print("foods in ascending alphabetical order:")
display_list(foods)

#append new foods to the original list
foods.append("carrots")
foods.append("milk")

#display the list with new items appended
print("sorted foods with carrots and milk appended to end:")
display_list(foods)

#sort the list in ascending alphabetical order
foods.sort()
print("foods in ascending alphabetical order:")
display_list(foods)

#find the index of "pizza" in the list
pizza_index = foods.index("pizza")
print(f"Pizza is at {pizza_index}")

#insert "fries" at the position of "pizza"
foods.insert(pizza_index, "fries")
pizza_index = foods.index("pizza")
print(f"Pizza is now at {pizza_index}")