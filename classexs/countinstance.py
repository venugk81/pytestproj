class Student:
    count =0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
    @classmethod
    def instance_count(self):
        return self.count

    def check_count(self):
        print("Count: ", self.instance_count())

stu=Student("John", 18)
stu.check_count()
stu.check_count()
stu=Student("John", 18)
stu.check_count()