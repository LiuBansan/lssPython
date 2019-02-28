
'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

'''

import time
import _thread as thread

def loop1():
    #ctime 得到当前之间
    print("start loop 1 at: ",time.ctime())
    time.sleep(4)
    print("end loop 1 at: ", time.ctime())

def loop2():
    #ctime 得到当前之间
    print("start loop 2 at: ",time.ctime())
    time.sleep(2)
    print("end loop 2 at: ", time.ctime())


def main():
    print("starting at: ", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行函数名，第二是函数的参数作为元组使用，为空则是用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("all done at: ", time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)