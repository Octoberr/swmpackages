# 前言
  自己常用的函数平常是在是太多了，经常会重复性编写
  
  索性就自己编写一个python包
  
  create by swm 2018/11/20
  
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
  
### 2018/11/20
增加判断操作系统的方法

修改名字为swmtools

help(swmtools.manytools)查看目前已有方法

### 2019/03/26
新增了xml，xlsx，csv文件的读取方法，help(readmanyfile)查看具体使用

新增了时间的处理方法，增加了一个计算当前方法运行时间的装饰器，使用help(timeformat)查看具体使用

### 2021/06/16
新增了单例日志方法，在logging的基础上完成

使用方法
```python
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
```
### 使用方法
线下安装：python setup.py bdist_wheel

线上安装：

    测试版:
            pip install -i https://test.pypi.org/simple/swmtools
         
    正式版：
            pip install swmtools
### 一张图理解各种join的效果
Images:

![](./pics/join.png)

>图解各种join的效果

### 对996的看法
当初在大学学习编程时，可以通宵不睡，可以连续3天吃喝都在实验室，那个时候完全感觉不到累，
996不应该是企业强制加给我们的，而是我们在追求自己喜欢的生活中愿意花时间在上面的，
当生存花费了我们太多时间，我们必然是没有时间去提升自己的。
