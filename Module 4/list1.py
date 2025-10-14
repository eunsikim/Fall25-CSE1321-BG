def main():
    ages = [20, 21, 19]
    states = ["Georgia", "Florida", "Alabama", "S. Carolina", "N. Carolina", "Tennessee"]

    for state in states:
        print(state)

    us_states = [state for state in states]
    
    for state in us_states:
        print(state)

    for i in range(len(states)):
        print(states[i])

    if "Georgia" in states:
        print("The list \"states\" contains the value of \"Georgia\"")
    else:
        print("The list \"states\" does not contains the value of \"Georgia\"")

    print(states[::-1])


if __name__ == "__main__":
    main()