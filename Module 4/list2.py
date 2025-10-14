def main():
    list_A = [1, "hello world", 3.14]

    list_B = [True]

    list_B.extend(list_A)

    print(list_B)


if __name__ == "__main__":
    main()