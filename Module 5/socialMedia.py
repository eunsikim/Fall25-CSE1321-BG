class content:
    # Content Constructor Function
    def __init__(self, text, media):
        self.text = text
        self.media = media

class user:
    # User Constructor Function
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.contents = []

    # Function to add a new content
    def add_content(self, text, media):
        self.contents.append(content(text, media))

def main():
    # user1 = user()
    # user2 = user()

    # user1.username = "ekim54"
    # user2.username = "jdoe01"


    # content1 = content()
    # content1.text = "Hello World"
    # content1.media = "./user/img/vacation_1.jpeg"

    # print(user1.username)
    # print(user2.username)

    # print(content1.media)
    # print(content1.text)


    users = []

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Print users")
        print("4. Exit")

        option = int(input("Enter option: "))

        if option == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            password_2 = input("Enter Password Again: ")

            if password != password_2:
                print("Passwords dont match")

            users.append(user(username, password))
        elif option == 2:
            print("login successful")
            break
        elif option == 3:
            for u in users:
                print(u.username)
        elif option == 4:
            break

    while True:
        print(f"Welcome {users[0].username}")
        print("1. Add a new content")
        print("2. View content")
        option = int(input("Enter option: "))

        if option == 1:
            text = input("Enter text: ")
            media = input("Enter media: ")
            users[0].add_content(text, media)
        elif option == 2:
            for u in users[0].contents:
                print(u.media)
                print(u.text)
                print()


if __name__ == "__main__":
    main()