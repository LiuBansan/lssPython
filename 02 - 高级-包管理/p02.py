'''
import p01
stu = p01.Student("shasa", 19)

stu.say()

p01.sayHello()


'''
# 文件可以用数字开头命名，但是传送过来的文件当作一个变量使用，报错。
# 借助于importlib包可以实现导入以数字开头的模块
import importlib

# 相当于导入了一个叫01的模块并把导入模块赋值给了shasa
shasa = importlib.import_module("01")

stu = shasa.Student()
stu.say()
