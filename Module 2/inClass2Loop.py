def main():
    USERNAME = "admin"
    PASSWORD = "password123"

    hasLoggedIn = False

    attempts = 0

    while True:
        username_input = input("Username: ")
        password_input = input("Password: ")

        # Valid
        if USERNAME == username_input and PASSWORD == password_input:
            print("Login Successful")
            hasLoggedIn = True
            break
        # Username invalid
        elif USERNAME != username_input:
            print("Username incorrect")
        # Password invalid
        elif PASSWORD != password_input:
            print("Password incorrect")
        # Other issues
        else:
            print("Login Error") 
        
        attempts += 1

        print(f"This is attempt #{attempts}, you have {3 - attempts} attempts left!")

        if attempts == 3:
            break
    
    if hasLoggedIn:
        print(f"Welcome, {USERNAME}!")
    else:
        print(f"Try again in 2 hours")
    
    

if __name__ == "__main__":
    main()