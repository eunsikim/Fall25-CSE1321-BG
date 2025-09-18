def main():
    number = int(input("Enter a number: "))

    for i in range(number):
        output = ""

        if (i + 1) % 7 == 0:
            output += "Fizz"

        if (i + 1) % 8 == 0:
            output += "Buzz"

        if output == "":
            output += str(i + 1)
        
        print(output)

if __name__ == "__main__":
    main()