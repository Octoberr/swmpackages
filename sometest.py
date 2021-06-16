from swmtools import MyLogger
import threading
import time
from datetime import datetime


def ddd():
    logger = MyLogger()
    # print(logger.get_instance())
    # logger.logger.info()
    logger.info(f"Now time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


for i in range(0, 10):
    t = threading.Thread(target=ddd, args=())
    time.sleep(5)
    t.start()
