def main():
    ages = {
        "Alice": 20,
        "Bob": 21,
        "Charlie": 22
    }

    print(list(ages))
    print(ages.values())
    print(ages.items())

    ages["Bob"] = 50
    print(ages)

    ages["John"] = 30
    print(ages)

if __name__ == "__main__":
    main()