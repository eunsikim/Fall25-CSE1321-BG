def main():
    number = 3

    guess = 0

    while guess != number:
        guess = int(input("Enter a number between 1 - 10: "))

        if guess != number:
            print("Incorrect")
    
    print(f"Congratulations, the number was {number}")
    

if __name__ == "__main__":
    main()