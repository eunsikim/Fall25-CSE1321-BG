def main():
    # Non-Numeric Zero values results as `True`
    age = 29
    # Numeric Zero values results as `False` 
    zeroVar = 0

    # Print the actual value of `age`
    print(age)
    # Print the Truthy/Falsy value of `age`
    print(bool(age))

    print(zeroVar)
    print(bool(zeroVar))

    # Non-empty String values results to `True` 
    name = "John"
    # Empty String values results to `False` 
    message = ""
    print(name)
    print(bool(name))

    print(message)
    print(bool(message))


if __name__ == "__main__":
    main()