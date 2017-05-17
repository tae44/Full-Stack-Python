class Student:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.courseList = [] # 学过的课程列表
        self.log = []        # 学习记录

    def select(self, course):
        print('{}选择的课程是: {}'.format(self.name, course.name))
        course.teacher.teach(self, course)
        if course.name not in self.courseList:
            self.courseList.append(course.name)

    def learnWhat(self):
        print('{}学过的课程为: {}'.format(self.name, self.courseList))
