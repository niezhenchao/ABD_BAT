# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/23 21:09
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：函数的传值与传地址
"""


def fun1(y):
    """
    传值：根据python的内存管理机制
    :param y: 形参（其实是一个局部变量）
    :return:
    """
    y = 3
    print("函数里面的y：%d" % y)


# 实参
x = 2
fun1(x)
print("函数外面的x：%d" % x)


def func2(list2):
    """
    传地址：必须是容器遍历，一定不能直接对容器变量赋值
    :return:
    """
    # 如果对参数直接赋值，就是传值了
    # 直接对容器遍历赋值
    list2 = 4
    # 如果是改变容器变量里面的元素的值，就是传地址
    # list2[2] = 4
    print("函数外面的list2：%s" % list2)


list1 = [1,2,3,4]
func2(list1)
print("函数外面的list1：%s" % list1)
