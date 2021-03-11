# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/26 21:52
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：全局变量
"""
# 全局变量：定义在整个模块中，对整个模块起作用的变量，用global引用
x, y = 1, 2
print(1)


def func_1(x, y):
    print(x + y)


class MyGlobal:
    """
    测试全局变量
    """

    def func_2(self):
        """
        如果找不到全局变量
        :return:
        """
        # 使用global申明
        global x, y
        print(x + y)


if __name__ == '__main__':
    func_1(1, 1)
    myglobal = MyGlobal()
    myglobal.func_2()
