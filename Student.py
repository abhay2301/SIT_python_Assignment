class student:
    def __init__(self, name, roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def showdata(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        # print("Marks:",self.marks)
    def showmarks(self):
        print("Marks:",self.marks)

obj1 = student("ABHAY","1",99)
obj1.showdata()  
obj1.showmarks()  
#students=[]
# num_students = int(input("Enter the number of students: "))
# for i in range(num_students):
#     name = input(f"Enter the name of the student{i+1}: ")
#     roll = input(f"Enter the roll number of the student{i+1}: ")
#     #marks = list(map(int(input(f"Enter the marks of the student{i+1}: ").split())))
#     marks=[]
#     for i in range(0,1):
#         marks.append(int(input("Enter the marks of the student: ")))
#     #students.append(student(name,roll,marks))\
# obj1 = student(name,roll,marks)
# obj1.showdata()
