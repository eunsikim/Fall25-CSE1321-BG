# input/parameters: sum of the items, how many items
# output/return: the average of items 
def calc_avg(items, size):
    calculation = items / size
    return calculation

# input/parameters: the average of an item, weigh/worth of that item in the grade
def calc_weigh(item, weigh):
    return item * weigh

def getUnknownGrades(item: str, checkHighest: bool):
    if item == "lab":
        if checkHighest:
            return 800
    elif item == "assignment":
        if checkHighest:
            return 500
    elif item == "midterm":
        if checkHighest:
            return 100
    elif item == "final":
        if checkHighest:
            return 100
    return 0

def calc_final_grade(lab1, lab2, lab3, lab4, lab5, assignment1, assignment2, checkHighest: bool):
    labs = calc_weigh(calc_avg(lab1 + lab2 + lab3 + lab4 + lab5 + getUnknownGrades("lab", checkHighest), 13), 0.1)

    assignments = calc_weigh(calc_avg(assignment1 + assignment2 + getUnknownGrades("assignment", checkHighest), 7), 0.4)

    midterm = calc_weigh(getUnknownGrades("midterm", checkHighest), 0.2)
    
    final = calc_weigh(getUnknownGrades("final", checkHighest), 0.3)

    final_grade = labs + assignments + midterm + final

    return final_grade

# 13 Labs (10%), 7 Assignments (40%), Midterm (20%), and Final (30%)
def main():
    lab1 = 0
    lab2 = 80
    lab3 = 90
    lab4 = 100
    lab5 = 40

    assignment1 = 85
    assignment2 = 90
    
    final_grade = calc_final_grade(lab1, lab2, lab3, lab4, lab5, assignment1, assignment2, True)

    print(f"Your maximum grade for this class will be {final_grade:.2f}")

    final_grade = calc_final_grade(lab1, lab2, lab3, lab4, lab5, assignment1, assignment2, False)

    print(f"Your minimum grade for this class will be {final_grade:.2f}")


if __name__ == "__main__":
    main()