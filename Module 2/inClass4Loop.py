import random

def main():
    usr_score = 0
    comp_score = 0

    ct = "yes"

    while ct == "yes":
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
                usr_score += 1
            elif usr_choice == 'paper' and comp_choice == 'rock':
                print("User wins")
                usr_score += 1
            elif usr_choice == 'scissors' and comp_choice == 'paper':
                print("User wins!")
                usr_score += 1

            # Draws
            elif usr_choice == comp_choice:
                print("Draw")

            # User lose
            else:
                print("Computer wins")
                comp_score += 1
        
        print("SCORE")
        print(f"USER: {usr_score}")
        print(f"COMPUTER: {comp_score}")

        ct = input("Do you want to continue (yes/no): ").lower()


if __name__ == "__main__":
    main()