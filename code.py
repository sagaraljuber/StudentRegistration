# pOne.introduce()
#
# sOne = Student("Alenere", "Sdpt", "1E")
# sOne.introduce()
#
# eOne = Employee("Juber", "Andrei", 5000)
# eOne.introduce()


# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(self.name + " Created")
#
# name = input("Enter a name: ")
# pOne = Person(name)

class Student:
    def __init__(self, name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print("     Name: " + self.name)
        print("     Course: " + self.course)
        print("     Year: " + str(self.year))
        print("     Section: " + self.section)

listOfStudents = []

while True:
    name = input("Enter name: ")
    course = input("Enter course: ")
    year = input("Enter year: ")
    section = input("Enter section: ")
    s = Student(name,course,year,section)
    listOfStudents.append(s)
    print()
    choice = input("Create Another Student? [Y/Any Char] : ")
    if choice == "Y" or choice == 'y': pass
    else: break


i = 1
for student in listOfStudents:
    print()
    print("Student #" + str(i))
    student.introduce()
    i = i + 1