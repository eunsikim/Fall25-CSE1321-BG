import time

def main():
    # Parent loop
    for x in range(3):
        print(f"Parrent Loop: Iteration #{x}")

        print("We are going to start the child loop...")
        
        # Child loop
        for y in range(5):
            time.sleep(1)
            print(f"\tChild Loop: Iteration #{y}")

        print("Child loop has stopped...")
        time.sleep(1)
        



if __name__ == "__main__":
    main()