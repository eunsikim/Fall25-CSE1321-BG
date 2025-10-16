def main():
    states = ["Georgia", "Florida", "Carolina", "Alabama", "Carolina", "Tennessee"]

    # Count how many times "Carolina" appears in the list
    print(f"Carolina appears {states.count("Carolina")} times")

    # Get the index value of the first appearance of "Carolina"
    print(f"The first appearance of Carolina in the list is at index {states.index("Carolina")}")

    # Sorting the list
    print(states)
    print("We are going to sort the list...")
    states.sort()
    print(states)

    # Joining each value in the list as a string
    joinining_str = ", "
    print(joinining_str.join(states))
    
if __name__ == "__main__":
    main()