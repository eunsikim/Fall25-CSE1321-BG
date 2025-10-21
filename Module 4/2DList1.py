def main():
    myList = [1, 3.14, "Hello", "World", True, ("John", 33)]

    my2DList = [["Alice", 20], ["Bob", 28], ["Charlie", 23]]

    for element in my2DList:
        # for sub_element in element:
        #     print(sub_element)

        print(f"{element[0]} is {element[1]} years old.")

    
if __name__ == "__main__":
    main()