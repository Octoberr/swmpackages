# 前言
  自己常用的函数平常是在是太多了，经常会重复性编写
  
  索性就自己编写一个python包
  
  create by swm 2018/11/20

### 2018/11/20
增加判断操作系统的方法

修改名字为swmtools

help(swmtools.manytools)查看目前已有方法

### 2019/03/26
新增了xml，xlsx，csv文件的读取方法，help(readmanyfile)查看具体使用

新增了时间的处理方法免得以后记混，还有一个计算当前方法运行时间的装饰器

help(timeformat)查看具体使用



### 使用方法
线下安装：python setup.py bdist_wheel

线上安装：

    测试版:
            pip install -i https://test.pypi.org/simple/ swmtools
         
    正式版：
            pip install swmtools
