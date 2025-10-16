def main():
    states = ["Georgia", "Florida", "Alabama", "S. Carolina", "N. Carolina", "Tennessee"]

    states_2 = ["Washington"]

    states_2.extend(states)

    # Updating a list/changing a value in a list.

    # Print out all of the elements in the list
    for i in range(len(states_2)):
        print(f"{i} -> {states_2[i]}")

    # Ask the user for the index of the value to replace.
    # Ask the user the new value
    selected_index = int(input("Select an index: "))
    new_state = input("Enter the name of the state you want to replace it with: ")

    # Update the specified index with a new value
    states_2[selected_index] = new_state

    print(states_2)

    
if __name__ == "__main__":
    main()