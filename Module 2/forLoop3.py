def main():
    password = input("Enter Password: ")

    hasExcl = False
    hasAt = False
    hasNum = False

    # Checking for number
    for c in password:
        if c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
            hasNum = True
            break
    
    # Checking for special chars
    for c in password:
        if c == "!":
            hasExcl = True
        elif c == "@":
            hasAt = True

    # Checking length of password
    count = 0
    for c in password:
        count += 1

    hasLength = count >= 8

    isValid = hasExcl and hasAt and hasNum and hasLength

    if isValid:
        print("Your password is good!")
    if not hasLength:
        print("Invalid Password: Passwords must contain 8 characters or more")
    if not hasExcl and not hasAt:
        print("Invalid Password: Passwords must contain all special characters (!, @)")
    if not hasNum:
        print("Invalid Password: Passwords must contain a number (0 - 9)")

if __name__ == "__main__":
    main()