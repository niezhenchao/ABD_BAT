# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/16 21:04
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：if分支语句
"""
# # z = |x|
# x = int(input("x:"))
#
# if x >= 0:
#     # 如果x>=0，就执行这个子过程
#     z = x
# else:
#     # 否则，就走这个子过程
#     z = -x
# print(z)

x = int(input("x:"))
y = int(input("y:"))

# if x >= 0:
#     # 当x>=0的时候
#     if y >= 0:
#         # 当y大于0的时候
#         z = x + y
#     else:
#         z = x - y
# else:
#     if y >= 0:
#         z = -x + y
#     else:
#         z = -x - y

if x >= 0 and y >= 0:
    z = x + y
elif x >= 0 and y < 0:
    z = x - y
elif x < 0 and y >= 0:
    z = -x + y
else:
    z = -x - y

print(z)
