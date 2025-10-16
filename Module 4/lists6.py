def main():
    # Remove the first appearance of the value "Carolina"
    # (the one in between florida and alabama)
    states = ["Georgia", "Florida", "Carolina", "Alabama", "Carolina", "Tennessee"]

    states.remove("Carolina")
    states.remove("Carolina")

    print(states)

    
if __name__ == "__main__":
    main()