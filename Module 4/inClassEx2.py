def main():
    message = "Hello"

    # 0, 1, 2, 3, 4
    # 4, 3, 2, 1, 0
    index_val = len(message) - 1
    for i in range(len(message)):
        print(message[index_val], end="")
        index_val -= 1

    # print() 
    for c in message:
        print(c, end="")


if __name__ == "__main__":
    main()