def main():
    number = int(input("Enter a number: "))

    # Check if number is negative
    if number < 0:
        print("Your number is negative")
    # Check if number is zero
    elif number == 0:
        print("Your number is zero")
    elif number % 2 == 0:
        print("Your number is even")
    elif number % 2 == 1:
        print("Your number is odd")


if __name__ == "__main__":
    main()