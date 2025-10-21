def avg(grading_items):
    sum = 0

    for item in grading_items:
        sum += item

    return sum / len(grading_items)

def final_grade(lab, assignment, midterm, final):
    return lab * 0.1 + assignment * .4 + midterm * 0.2 + final * 0.3 

def main():
    student_list = [
        ["John", 89, 80, 91, 95, 70, 100, 80],
        ["Alice", 90, 70, 79, 80, 90, 100, 100]
    ]

    for student in student_list:
        print(student[0])
        lab = avg(student[1:4])
        assignment = avg(student[5:6])
        print(f"\tLab avg: {lab}")
        print(f"\tAssignment avg: {assignment}")
        print(f"\tMidterm exam: {student[6]}")
        print(f"\tFinal exam: {student[7]}")
        print(f"\tFinal Grade: {final_grade(lab, assignment, student[6], student[7])}")
        print()

    
if __name__ == "__main__":
    main()