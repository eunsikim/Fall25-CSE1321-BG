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
        if usr_choice == "rock":
            if comp_choice == "scissors":
                print("User wins")
            elif comp_choice == "paper":
                print("Computer wins")
            else:
                print("Draw")
        elif usr_choice == "paper":
            if comp_choice == "rock":
                print("User wins")
            elif comp_choice == "scissors":
                print("Computer wins")
            else:
                print("Draw")
        elif usr_choice == "scissors":
            if comp_choice == "paper":
                print("User wins")
            elif comp_choice == "rock":
                print("Computer wins")
            else:
                print("Draw")


if __name__ == "__main__":
    main()