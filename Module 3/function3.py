message = "Hello World"

def square_perimeter(side1, side2):
    print(message)
    message = 4
    print(f"Side 1 : {side1} , Side 2 : {side2}")
    return 2 * (side1 + side2)

def main():
    print(message)
    side1 = int(input("Enter length of one side: "))
    side2 = int(input("Enter length of another side: "))

    print(square_perimeter(side2, side1))
    
    
if __name__ == "__main__":
    main()