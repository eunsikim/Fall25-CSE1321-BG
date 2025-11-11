class NumberNotEven(Exception): # Inheritance, this is a 1322 concept. Disregard.
    def __def__(self, message = ""):
        super().__init__(message)

def main():
    evenNumbers = []

    while True:
        try:
            number = int(input("Enter an even number (or -1 to STOP): "))
            if number == -1:
                break
            
            if number % 2 == 0:
                evenNumbers.append(number)
            else:
                raise NumberNotEven(f"Please enter even numbers, {number} is not even")
        except NumberNotEven as error:
            print(error)
        except ValueError:
            print("Please enter integer values only")

    while True:
        try:
            for i in range(len(evenNumbers)):
                print(f"{i} -> {evenNumbers[i]}")
            
            option = int(input("Enter an index (or -1 to STOP): "))
            if option == -1:
                break

            print(f"You chose the number {evenNumbers[option]}")
        except ValueError:
            print(f"Please enter integer values only")
        except IndexError:
            print(f"That index does not exist, please enter numbers from 0 to {len(evenNumbers) - 1}. Or, -1 to STOP")


if __name__ == "__main__":
    main()