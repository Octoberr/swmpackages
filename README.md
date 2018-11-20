# 前言
  自己常用的函数平常是在是太多了，经常会重复性编写
  
  索性就自己编写一个python包
  
  create by swm 2018/11/20

### 2018/11/20
增加判断操作系统的方法

修改名字为swmtools

help(swmtools.manytools)查看目前已有方法


### 使用方法
线下安装：python setup.py bdist_wheel

线上安装：

    测试版:
            pip install -i https://test.pypi.org/simple/ swmtools
         
    正式版：
            pip install swmtools