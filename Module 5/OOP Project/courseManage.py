import course as c

class courseManager:
    def __init__(self):
        self.courseList = []

    def add_course(self, fm): #fm: Faculty Manager obj.
        crn = input()
        name = input()
        time = input()

        for i in range(len(fm.faculty_list)):
            print(f"{i} -> {fm.faculty_list[i].name}")
        
        option = input()

        instructor = fm.faculty_list[option]

        new_course = c.course(crn, name, time, instructor)

        self.courseList.append(new_course)

    def edit_course(self):
        pass

    def remove_course(self):
        pass

    def register_course(self, student):
        for i in range(len(self.courseList)):
            print(f"{i} -> {self.courseList[i].name} - {self.courseList[i].time} - {self.courseList[i].instructor.name}")
        
        option = input()

        course = self.courseList[option]

        course.gradebook[student] = ""
        student.classlist.append(course)
