def helloWorld():
    print("Hello World")

def addition(n1, n2):
    sum = n1 + n2

    return sum

def main():
    while True:
        print("Press 1 for Hello World")
        print("Press 2 for Addition")
        print("Press X to quit")
        option = input("> ")

        print(option)

        if option == "1":
            helloWorld()
        elif option == "2":
            number1 = int(input("Enter a number: "))
            number2 = int(input("Enter another number: "))

            print(addition(number1, number2))
        elif option == "X":
            break

if __name__ == "__main__":
    main()