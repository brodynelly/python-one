import random
import pickle

def save_game(player):
    try:
        with open(f"{player['name']}.rps", "wb") as file:
            pickle.dump(player, file)
            print(f"{player['name']}, your game has been saved.")
    except Exception as e:
        print(f"Sorry {player['name']}, the game could not be saved.")
        print(e)

def load_game(name):
    try:
        with open(f"{name}.rps", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"{name}, your game could not be found.")
        return None
    except Exception as e:
        print("Error loading game:", e)
        return None

def display_statistics(player):
    print(f"{player['name']}, here are your game play statistics...")
    print(f"Wins: {player['wins']}")
    print(f"Losses: {player['losses']}")
    print(f"Ties: {player['ties']}")
    if player['losses'] > 0:
        win_loss_ratio = player['wins'] / player['losses']
        print(f"Win/Loss Ratio: {win_loss_ratio:.2f}")
    else:
        print("Win/Loss Ratio: N/A")

def play_game(player):
    choices = ["Rock", "Paper", "Scissors"]
    round_number = player['wins'] + player['losses'] + player['ties'] + 1

    print(f"\nRound {round_number}")
    print("1. Rock\n2. Paper\n3. Scissors")
    user_choice = input("What will it be? ")

    if user_choice.isdigit() and int(user_choice) in range(1, 4):
        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)
        print(f"\nYou chose {user_choice}. The computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
            player['ties'] += 1
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win!")
            player['wins'] += 1
        else:
            print("You lose!")
            player['losses'] += 1
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

def start_new_game():
    name = input("What is your name? ")
    player = {'name': name, 'wins': 0, 'losses': 0, 'ties': 0}
    print(f"Hello {player['name']}. Let's play!")
    while True:
        play_game(player)
        action = input("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Quit\nEnter choice: ")
        if action == "2":
            display_statistics(player)
        elif action == "3":
            save_game(player)
            break

def load_existing_game():
    name = input("What is your name? ")
    player = load_game(name)
    if player:
        print(f"Welcome back {player['name']}. Let's play!")
        while True:
            play_game(player)
            action = input("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Quit\nEnter choice: ")
            if action == "2":
                display_statistics(player)
            elif action == "3":
                save_game(player)
                break

print("\nWelcome to Rock, Paper, Scissors!")
while True:
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        start_new_game()
    elif choice == "2":
        load_existing_game()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
