
'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

'''

import time
def loop1():
    #ctime 得到当前之间
    print("strat loop 1 at: ",time.ctime())
    time.sleep(4)
    print("end loop 1 at: ", time.ctime())

def loop2():
    #ctime 得到当前之间
    print("strat loop 2 at: ",time.ctime())
    time.sleep(2)
    print("end loop 2 at: ", time.ctime())


def main():
    print("strating at: ", time.ctime())
    loop1()
    loop2()
    print("all done at: ", time.ctime())


if __name__ == '__main__':
    main()