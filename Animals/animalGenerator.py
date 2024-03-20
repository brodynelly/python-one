
from Animal import Animal

def main():
    print("Welcome to the animal generator!")
    print("This program creates Animal objects.")

    animals = []

    while True:
        animal_type = input("\nWhat type of animal would you like to create? ")
        name = input("What is the animal’s name? ")
        animals.append(Animal(animal_type, name))

        add_more = input("\nWould you like to add more animals (y/n)? ")
        if add_more.lower() != 'y':
            break

    print("\nAnimal List:")
    for animal in animals:
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")

if __name__ == "__main__":
    main()