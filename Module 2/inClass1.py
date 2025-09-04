def main():
    age = int(input("Enter age: "))

    if age < 18:
        print("You are not allowed to vote yet")
    else:
        print("You are allowed to vote")

    # if age >= 18:
    #     print("You are allowed to vote")
    # else:
    #     print("You are not allowed to vote yet")

if __name__ == "__main__":
    main()