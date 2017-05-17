import course_homework.admin as admin
import course_homework.student as student

t1 = admin.Teacher('jeff', '男', 22) # 创建老师
t2 = admin.Teacher('jane', '女', 20)

c1 = admin.Course('语文', '1小时', 25, t1) # 创建课程
c2 = admin.Course('数学', '2小时', 35, t2)

s1 = student.Student('A', '男', 15) # 创建学生
s2 = student.Student('B', '男', 16)

print('课程名称: {}   授课老师: {}   课时费: {}'.format(c1.name, c1.teacher.name, c1.money))
print('课程名称: {}   授课老师: {}   课时费: {}'.format(c2.name, c2.teacher.name, c2.money))

s1.select(c1) # 学生选课
s2.select(c2)

t1.howmany() # 查询老师资产
t2.howmany()

s1.learnWhat() # 查询学过什么课程
s2.learnWhat()
