def isEven(number):
    calculation = number % 2

    if calculation == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is odd")


def main():
    for i in range(1, 101):
        isEven(i)

if __name__ == "__main__":
    main()