def getUserInfo():
    name = input("Name: ")
    age = int(input("Age: "))

    return name, age

def main():
    age, name = getUserInfo()

    print(f"Name: {name}, Age: {age}")

    
if __name__ == "__main__":
    main()