from unicodedata import name


class ClassStudent:
    def __init__(self):
        self.name = None
        self.class_name = None

    def register(self, class_name):
        self.class_name = class_name

student_one = ClassStudent()
student_one.name = 'Trung'
student_one.class_name = 'Python2022'


student_one.register('trungbk225')
print(type(student_one))