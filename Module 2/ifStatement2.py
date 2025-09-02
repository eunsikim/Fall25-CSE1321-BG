def main():
    # Password must have 8 or more characters.
    # Password must contain ! and @
    password = input("Enter a password: ")

    # isValid = len(password) >= 8
    # isValid = '!' in password and '@' in password
    isValid = (len(password) >= 8) and ('!' in password and '@' in password)

    if isValid:
        print("Your password is good!")
    else:
        print("Passwords must be 8 characters or more and contain special characters (!, @)")



if __name__ == "__main__":
    main()