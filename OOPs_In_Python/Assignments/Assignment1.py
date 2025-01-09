
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def printStudents(self):
        print(self.students)

if __name__ == "__main__":
    a = Student('Alice', 22)

    c = Course("Math", 5)

    c.addStudent(a)

    print(len(c.students))

    for i in c.students:
        print(i)
        print(i.name)
        print(i.age)