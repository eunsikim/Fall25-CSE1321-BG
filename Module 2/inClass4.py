import random

def main():
    # User Input
    usr_choice = input("Enter one choice (rock, paper, scissors): ").lower()

    # Input validation
    if usr_choice != "rock" and usr_choice != "paper" and usr_choice != "scissors":
        print("Wrong choice")
    else:
        # Computer's choice (Rock, Paper, Scissors)
        options = ["rock", "paper", "scissors"]
        comp_choice = random.choice(options)
        print(f"Computer chosed {comp_choice}")

        # Logic
        # User win
        if usr_choice == 'rock' and comp_choice == 'scissors':
            print("User wins")
        elif usr_choice == 'paper' and comp_choice == 'rock':
            print("User wins")
        elif usr_choice == 'scissors' and comp_choice == 'paper':
            print("User wins!")

        # Draws
        elif usr_choice == comp_choice:
            print("Draw")

        # User lose
        else:
            print("Computer wins")

if __name__ == "__main__":
    main()