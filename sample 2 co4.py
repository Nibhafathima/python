class Personal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student name:", self.name)
        print("Student age:", self.age)


class Qualification:
    def __init__(self, degree_name, total_marks, percentage):
        self.dname = degree_name
        self.marks = total_marks
        self.percentage = percentage

    def display(self):
        print("Degree:", self.dname)
        print("Total Marks:", self.marks)
        print("Percentage:", self.percentage)


obj_person = Personal("minu", 21)
obj_quali = Qualification("BCA", 500, 70.0)

obj_person.display()
obj_quali.display()