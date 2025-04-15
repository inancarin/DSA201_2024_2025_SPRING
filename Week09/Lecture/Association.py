from person import Person

class Student(Person):
    def __init__(self, name, id, age):
        super().__init__(name, id, age)
        self.courses = []
    
    def printCourses(self):
        if len(self.courses) == 0:
            print("No enrolled course for this student")
        else:
            print("The courses studentID", self.id,  ",", self.name, "enrolled in:")
            for course in self.courses:
                print(course)

    def registerCourse(self, course):
        if course.availableSlot():
            course.incrNumberOfStudents()
            self.courses.append(course)
            print(self.name, "registered to", course.code)
        else:
            print("No available slot for", course.code)


class FacultyMember(Person):
    def __init__(self, name, id, age):
        super().__init__(name, id, age)
        self.courses = []
    
    def teachCourse(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, crn, code, capacity, instructors):
        self.crn = crn
        self.code = code
        self.capacity = capacity
        self.enrolledStudentNumber = 0
        self.instructors = instructors
    
    def __str__(self):
        return "CRN: " + str(self.crn) + ", Code: " + self.code + ", Capacity: " + str(self.capacity)
    
    def availableSlot(self):
        return self.capacity > self.enrolledStudentNumber

    def incrNumberOfStudents(self):
        if self.enrolledStudentNumber < self.capacity:
            self.enrolledStudentNumber += 1
        else:
            print("Error")
    
    def increaseCapacity(self, additionalCapacity):
        self.capacity += additionalCapacity


# main
if100 = Course(1, "IF100", 2, ["Inanc", "Duygu"])
sps101 = Course(2, "SPS101", 1, ["Emre Erol"])

s1 = Student("Jack", 1, 19)
s2 = Student("Alice", 2, 20)
s3 = Student("Rose", 3, 19)

s1.registerCourse(if100)
s1.registerCourse(sps101)
s2.registerCourse(if100)
s2.registerCourse(sps101)
s3.registerCourse(if100)
if100.increaseCapacity(1)
s3.registerCourse(if100)
s1.printCourses()

f1 = FacultyMember("Inanc", 1, 70)
f1.teachCourse(if100)