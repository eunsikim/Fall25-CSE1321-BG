def main():
    # When we use range with a single argument, 
    # the argument is the exclusive end range  
    for number in range(10):
        print(number)

    # When we use range with two arguments,
    # the first argument is the inclusive start
    # and the second argument is the exclusive end.
    for number in range(4, 10):
        print(number)

if __name__ == "__main__":
    main()