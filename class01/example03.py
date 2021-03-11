# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/14 21:05
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：数据类型
"""
# 整数:int（大整数）
x = -11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
print(type(x))
print(x)

# 小数：float（双精度，15或者16位有效数字）
y = 1.1111111111111111111111111111111111111111
print(type(y))
print(y)

# 字符串：str
s = 'dsfjds啊啊jafi'
print(type(s))

# 布尔值：bool(只有两个值：True，False)
b = False
print(type(b))

z = -0.1
# (为0，不为0)
if z:
    print(1)

s = '1'
# (为空，不为空)
if s:
    print('yes')

# 空：None
# 在使用一个变量或者对象之前，需要先判空
x = None
if x:
    print(x+1)


