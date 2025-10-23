def main():
    my_tuple = (("x", 1), ("y", 2) )
    my_list = [["x", 1], ["y", 2]]
    my_list_tuple = [("x", 1), ("y", 2)]

    print(dict(my_tuple))
    print(dict(my_list))
    print(dict(my_list_tuple))

if __name__ == "__main__":
    main()