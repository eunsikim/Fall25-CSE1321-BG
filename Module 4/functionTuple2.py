def someFunction(*params, name, age):
    print(f"Name: {name}, Age: {age}")

    for i in params:
        print(i)

def main():
    someFunction("Hello World", 1, 2, 3.14, age = "Eun Sik", name = 29, )

    
if __name__ == "__main__":
    main()