def main():
    USERNAME = "admin"
    PASSWORD = "password123"

    while True:
        username_input = input("Username: ")
        password_input = input("Password: ")

        # Valid
        if USERNAME == username_input and PASSWORD == password_input:
            print("Login Successful")
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
    
    print(f"Welcome, {USERNAME}!")

if __name__ == "__main__":
    main()