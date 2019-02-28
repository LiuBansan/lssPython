import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        print("pull", item, "out of q") # 此处替换为有用的工作
        input_q.task_done() #发出星号通知完成
    print("out of consumer:", ctime())
    ##此句未执行，因为q.join()收集到四个task_done()信号后，主进程启动，未等到print此句完成，程序就结束了

def producer(sequence, output_q):
    print("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of producer:", ctime())


# 简历进程
if  __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target = consumer, args = (q, ))
    cons_p.daemon = True
    cons_p.start()

    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在时间中忙着可能是生成器的输出或通过一些其它啊方式生产出来
    sequence = [1,2,3,4]
    producer(sequence, q)
    # 等待所有项被处理
    q.join()

