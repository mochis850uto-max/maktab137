class student:
    def __init__(self, name,grade):
        self.name = name
        self.grade = []
    def add_grade(self,*args):
        for arg in args:
            self.grade.append(arg)
        print(self.grade)
    def average(self):
        result =  sum(self.grade)/len(self.grade)
        print(result)

students = student("alice",25)
students.add_grade(18, 14, 13, 18 )

students.average()
