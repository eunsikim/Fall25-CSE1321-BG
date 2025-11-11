def main():
    # while True:
    try:
        x = int(input("Enter a number (-1 to break, DO NOT ENTER 7): "))
        
        if x == 7:
            raise Exception()
        
        print(f"You entered the number {x}")

        

        # if x == -1:
        #     break
    except Exception:
        print("You should input only integer numerical values.")
    finally:
        print("Executing finally block...")
    
    print("Program Terminated")

if __name__ == "__main__":
    main()