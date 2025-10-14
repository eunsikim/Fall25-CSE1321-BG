def approach1():
    age1 = int(input("Enter age 1: "))
    age2 = int(input("Enter age 2: "))
    age3 = int(input("Enter age 3: "))
    age4 = int(input("Enter age 4: "))
    age5 = int(input("Enter age 5: "))
    age6 = int(input("Enter age 6: "))
    age7 = int(input("Enter age 7: "))
    age8 = int(input("Enter age 8: "))
    age9 = int(input("Enter age 9: "))
    age10 = int(input("Enter age 10: "))

    average = age1 + age2 + age3 + age4 + age5 + age6 + age7 + age8 + age9 + age10
    average /= 10

    print(f"The average age of class A is {average:.2f}")

def approach2():
    sum = 0
    for i in range(120):
        sum += int(input(f"Enter age {i + 1}: "))
    sum /= 10
    print(f"The average age of class A is {sum:.2f}")


def main():
    print("Approach 1:")
    approach1()

    print("\nApproach 2:")
    approach2()

if __name__ == "__main__":
    main()