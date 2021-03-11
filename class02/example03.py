# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/16 20:17
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：逻辑运算
"""
################ 逻辑运算 ##################
# bool值的运算：not and or
"""
and：而且
or ：或者
not：不是
实例：判断x是正整数且小于100
and：真真为真，有假为假
or ：假假为假，有真为真
not：取反
"""
# x = int(input("请输入x的值："))
# b1 = x > 0
# print(b1)
# b2 = x < 100
# print(b2)
# print(b1 and b2)

# # 优先级：not>and>or
# b1 = True
# b2 = True
# b3 = False
# # not>and
# print(b2 and not b1)
# # and>or
# print(b2 or b1 and b3)

# 短路原则
"""
and：False and 任何都不成立，and 后的语句是不执行
or ：True or 任何都是成立的，所以or后面的语句是不执行的
"""
x = 1
y = 2
z = 2
print(x > y and y == z)
print(x < y or y == z)

