def main():
    option = ""

    while option != "exit":
        print("1 -> To perform a Hello World")
        print("exit -> Stop the program")

        option = input("> ")

        if option == "1":
            print("Hello World")

if __name__ == "__main__":
    main()