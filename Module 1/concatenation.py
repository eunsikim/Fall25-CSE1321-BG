def main():
    # Concatenation with just strings
    text1 = "Hello"
    text2 = "World"
    fullText = "Hello " + "World"
    print(text1 + " " + text2)
    print(text1 + " world")
    print(fullText)

    # Concatenation with other types
    number = 123

    preparedNumber = str(number) # 123 => "123"

    preparedString = fullText + " " + preparedNumber

    print(fullText + " " + preparedNumber)
    print(fullText + " " + str(number))
    print(preparedString)

    preparedString = "Hello World"

    print()

    print(fullText + " " + preparedNumber)
    print(fullText + " " + str(number))
    print(preparedString)


if __name__ == "__main__":
    main()