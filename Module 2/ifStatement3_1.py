def main():
    # Valid Passwords must have 8 or more characters.
    # Valid Passwords must contain ! and @
    # Valid Passwords must contain a number 
    password = input("Enter a password: ")

    # isValid = len(password) >= 8
    # isValid = '!' in password and '@' in password
    isValidLenght = len(password) >= 8
    containSpecChar = '!' in password and '@' in password
    containNumber = '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password or '0' in password

    isValid = isValidLenght and containSpecChar and containNumber

    if isValid:
        print("Your password is good!")
    if not isValidLenght:
        print("Invalid Password: Passwords must contain 8 characters or more")
    if not containSpecChar:
        print("Invalid Password: Passwords must contain all special characters (!, @)")
    if not containNumber:
        print("Invalid Password: Passwords must contain a number (0 - 9)")



if __name__ == "__main__":
    main()