class course:
    def __init__(self, crn, name, time, instructor):
        self.crn = crn
        self.name = name
        self.time = time
        # TODO: Figure out where to add the schedule conflict check logic
        self.instructor = instructor

        self.gradebook = {}