def main():
    states = ("Georgia", "Florida", "Carolina", "Alabama", "Carolina", "Tennessee")

    for s in states:
        print(s)

    states_2 = tuple(["Texas"])

    states += states_2

    print(states)

    states_list = list(states)

    del states_list[0]

    states = tuple(states_list)

    print(states)

    
if __name__ == "__main__":
    main()