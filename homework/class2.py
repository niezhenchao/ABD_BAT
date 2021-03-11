# -*- coding: UTF-8 -*-
from decimal import Decimal

print('############################下面是结果###########################')
#
# # 将课程九九乘法表，以while循环实现
# # 两个数相乘，都是从1-9递增
# # 先控制x循环递增到9
# print('# 将课程九九乘法表，以for循环实现')
# for x in range(1, 10):
#     # 在循环里面，再控制y循环递增到9
#     # 每一个x都会和9个y相乘
#     # 定义每行显示的内容
#     # ''代表长度为0的字符串，就是没有字符
#     row = ''
#     for y in range(1, 10):
#         row += str(y) + "x" + str(x) + "=" + str(x * y) + '\t'
#         # if x == y:
#         #     break
#
#     print(row)
#     x += 1

# print()
# # 四舍五入保留两位小数
# print('# 四舍五入保留两位小数')
# f = 100.0000
# print(round(f, 2))
# f = '%.2f' % f
# print(f)
# f = 100.5555
# print(Decimal(f))
# print(round(f, 3))
# f = '%.3f' % f
# print(f)
# f = 100.5555
# f = Decimal(str(f)).quantize(Decimal('0.000'))
# print(f)

# print()
# # 用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？
# print('用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？')
# # 判断字符串长度的函数：len()
# print('请在此输入用户名：')
# loginname = input()
# password = input()
# # Python里面空指针是None，不是null
# #loginname = None
#
# if (not(loginname is None) and not(password is None)) \
#     and (6 < len(loginname) < 17 and 6 < len(password) < 17):
#     print('用户名密码合法')
# else:
#     print('用户名密码非法')
#

# print()
# # 九九乘法表去掉对角线
# print('# 九九乘法表去掉对角线')
# x = 1
# while x < 10:
#     row = ''
#     y = 0
#     while y < 9:
#         y += 1
#         # 第一条对角线条件是x==y
#         # 第二条对角线条件是x+y==10
#         if x == y or x + y == 10:
#             row += '' + '\t\t'
#         else:
#             row += "x*y=" + str(x * y) + '\t'
#
#     print(row)
#     x += 1

# print('\n'.join([' '.join(["%1sx%1s = %-2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

s = ''
for i in range(1, 10):
    s1 = ''
    for j in range(1, i + 1):
        s1 += "%1sx%1s = %-2s" % (j, i, i * j) + " "

    s += s1 + "\n"

print(s)
