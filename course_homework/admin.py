import time

class Teacher:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.__money = 0

    def teach(self, student, course):
        print('{}正在教{}{}...'.format(self.name, student.name, course.name))
        time.sleep(2)
        print('课时结束! {}赚了{}课时费~'.format(self.name, course.money))
        self.__money += course.money

    def howmany(self):
        print('{}现有资产为{}元'.format(self.name, self.__money))

class Course:
    def __init__(self, name, time, money, teacher):
        self.name = name
        self.time = time
        self.money = money
        self.teacher = teacher
