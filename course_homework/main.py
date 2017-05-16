import course_homework.admin as admin
import course_homework.student as student

t1 = admin.Teacher('jeff', '男', 22)
t2 = admin.Teacher('jane', '女', 20)

c1 = admin.Course('语文', '1小时', 25, t1)
c2 = admin.Course('数学', '2小时', 35, t2)


