# DO NOT STUDY THIS, THIS IS JUST AN EXAMPLE




















def main():
    # Name, Test 1, Test 2, Assignment 1, Assignment 2
    student_data = [
            ['John', 80.0, 75.0, 90.0, 100.0],
            ['Alice', 89.0, 80.0, 75.0, 80.0]
        ]
    
    # print(student_data[0])

    # for x in range(len(student_data)): # range(2)
    #     print(student_data[x])

    print(student_data[0][0])

    # Calculate Final Grade
    # Tests 60%, Assignments 40%
    for x in range(len(student_data)):
        test = 0
        assignemnt = 0

        for y in range(len(student_data[x])):
            if y > 0:
                if y < 3:
                    test += student_data[x][y]
                elif y >= 3:
                    assignemnt += student_data[x][y]

        final_grade = (test / 2 * 0.6) + (assignemnt / 2 * 0.4)
        print(f"{student_data[x][0]} has a final grade of {final_grade}")
    print()
    print("Name\tT1\tT2\tA1\tA2")
    for student in student_data:
        for data in student:
            print(data, end="\t")

        print()

            



if __name__ == "__main__":
    main()