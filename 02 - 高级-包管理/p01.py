# 包含一个学生类，一个sayHello函数
# 一个打印函数

class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age


    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi, 欢迎")

# 做一个判断，如果是自己调用就执行，否则不执行
# 此判断语句建议一直作为程序入口
if __name__ == "__main__":
    print("我是模块p01，你叫我干啥啊")

a = Student("ss",12)
a.say()
sayHello()






