# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/26 21:44
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：局部变量
"""
# 定义在函数中，只在当前函数中起作用的变量
# 在某个缩进的过程里面定义的变量，我们称为局部变量
# 原则上讲，超过这个缩进，这个变量就不能被使用了
x = 3
y = 2
if x > y:
    z = 1
    print(z)
else:
    zz = 2
    print(zz)
