# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/23 21:30
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：递归
"""


# 求n!：1!=1, n! = n*(n-1)!
def facs(n):
    # 出口
    if n <= 1:
        return 1

    # n！=n*(n-1)!
    s = n * facs(n - 1)
    # 返回n!的阶乘的值
    return s


print(facs(4))
