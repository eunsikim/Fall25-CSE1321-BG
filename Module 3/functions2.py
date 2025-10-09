import functions2_lib as f2l

def main():
    while True:
        option = f2l.menuOption()

        if option == "1":
            f2l.helloWorld()
        elif option == "2":
            f2l.additionHandler()
        elif option == "X":
            break



if __name__ == "__main__":
    main()