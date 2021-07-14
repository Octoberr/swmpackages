import os
import time
from multiprocessing import Manager, Pool  # 修改import中的Queue为Manager


def reader(q):
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    for i in "helloword":
        q.put(i)


if __name__ == "__main__":
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool(3)
    po.apply_async(writer, (q,))

    for i in range(3):
        po.apply_async(reader, (q,))
        time.sleep(5)

    po.close()
    po.join()
    print("(%s) End" % os.getpid())
