def main():
    string1 = "Hello World"
    string2 = "heLlo WoRld"

    # To make the comparison operator "Case Insensitive"
    # we need to sanitize the variables
    string1 = string1.lower() # => hello world
    string2 = string2.lower() # => hello world

    if string1 == string2:
        print("Both strings are the same")
    else:
        print("Both strints are not the same")


if __name__ == "__main__":
    main()