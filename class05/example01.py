# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/23 20:10
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：函数
"""


# 实现输入两个数，返回两个数的和的功能
def addInt(x, y):
    """
    描述函数的功能：实现输入两个数，返回两个数的和的功能
    括号表示参数列表，多个参数用逗号分隔
    参数是什么？它是函数运行需要用到的数据
    返回是什么？是函数返回给我们处理后的数据
    :param x: 第一个数
    :param y: 第二个数
    :return: 两个数的和的绝对值
    """
    # 处理
    z = x + y
    if z > 0:
        # 返回
        return z
    else:
        return -z
    # 函数只要return了，就代表执行完了，return后面的代码是不执行的
    print(1)


if __name__ == "__main__":
    # 只有直接执行这个py文件的时候才执行里面代码
    # 如果是作为库导入，是不会执行
    # 所以这里面一般会写这个模块里面的功能的测试或者示例代码

    # 函数的执行
    # 获取函数的返回结果
    r = addInt(-2,1)

    print("here")
