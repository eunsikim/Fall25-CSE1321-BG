def main():
    states = ["Georgia", "Florida", "Alabama", "S. Carolina", "N. Carolina", "Tennessee"]

    # Delete by index
    del states[0]
    print(states)

    # Delete by index, and also get the value that was deleted
    print(f"We just removed the value: {states.pop(1)}")
    print(states)
    
if __name__ == "__main__":
    main()