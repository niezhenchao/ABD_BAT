# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/14 20:33
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：基础语法
"""
# 逗号：枚举，并列，一一对应
a, b, c = 1, 2, 3
print(a)
# 等号：赋值，把某一个值给到一个变量，设x=1
x = 1
print(x)


# 括号：函数的参数部分，元组的定义，优先级
def sum(x, y):
    print(x)
    return x + y


# 单引号，双引号：都代表字符串
s, s1 = 'aa', "b"

# 取余：%
print(17 % 3)

# 幂运算：**
print(2 ** 3)

# 整除：//
print(17 // 3)

# 赋值叠加运算
x = 1
# x = x + 1
x += 1
print(x)

# 逻辑运算：比较运算
print(1 == 2)
