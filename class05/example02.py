# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/23 20:21
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：函数的参数详解
"""


def my_fun(x, y, *args, a=1, b=2, **kwargs):
    """
    1.固定参数（必填参数）：x,y
        必须传入的参数，如果没有指定（参数名字=值）这样的形式传入，那么就按顺序一一对应
        如果有指定（参数名字=值），就会按名字对应传入

    2.可变参数（非必填参数）：a=3,b=4
        有默认值的参数，我们称为可变参数
        可变参数可以不传，不传的时候使用定义时的默认值
        两种传入方式：按顺序传，按参数名传
        它必须定义在固定参数的后面

    3.可变参数列表：*args
        是指把除了固定参数传入的参数外的参数，当做一个元组
        不能写在非必填参数的前面
        非必填参数需要写在*args的后面
            非必填参数，必须按参数名传入

    4.非必填参数字典（可变参数字典）：**kwargs
        传入的键值对参数，会被转为字典
        必须出现在*args，和非必填参数的后面

    :return:
    """
    print("固定参数：")
    print(x, y)
    print(a, b)
    print(args)
    print(kwargs)


my_fun(1, 2, 3, 4, 5, 6, 7, 8, 9, a=1, b=2, c=3, d=4)


# 指针传参
def my_fun_1(x, y, z):
    """
    固定参数或者*args
    :param x:
    :param y:
    :param z:
    :return:
    """
    print(x + y + z)


l_p = [2, 3, 4]
my_fun_1(*l_p)


def my_fun_2(a=0, b=0):
    """
    非必填参数或者**kwargs
    :param a:
    :param b:
    :return:
    """
    print(a, b)


d_p = {'a': 1, 'b': 2}
my_fun_2(**d_p)


# 返回
def my_fun_3():
    """
    你返回的是什么，你得到的就是什么
    可以返回所以基本数据类型，和所有数据结构，以及对象
    :return:
    """
    return [1.1, ]


print(type(my_fun_3()))
