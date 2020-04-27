class SchoolMember:
    '''代表学校的任何成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(初始化学校成员：{})'.format(self.name))

    def tell(self):
        '''告诉我细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    '''代表老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(初始化老师：{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(初始化学生：{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一个空行
print()

members = [t, s]
for member in members:
    # 为Teachers和Students工作
    member.tell()
