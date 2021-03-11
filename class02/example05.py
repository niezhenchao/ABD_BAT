# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/16 21:04
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：while循环
"""
# 每个月上半个月每天我们都上java，下半个月每天我们都上Python
# 需求：打印每个月每一天我在干什么

# # 先以10月为例
# # 每个月从1号开始
# x = 1
#
# while x <= 31:
#     if x <= 15:
#         print(str(x) + '号上java课')
#     else:
#         print(str(x) + '号上python课')
#
#     # 每次循环后，x都要加1天
#     x += 1

# 打印今年每一天will在干什么
y = 1
while y <= 12:
    # 确定每个月的天数
    # 二月份：
    if y == 2:
        days = 29
    else:
        # 31天的有哪些情况？
        # y<=7的时候的奇数，和y>=8的偶数
        if (y <= 7 and (y % 2) == 1) or (y >= 8 and (y % 2) == 0):
            days = 31
        else:
            days = 30

    # 添加每个月要干什么
    x = 1
    while x <= days:
        if x <= 15:
            print(str(x) + '号上java课', end="；")
        else:
            print(str(x) + '号上python课', end="；")

        # 每次循环后，x都要加1天
        x += 1

    # 换行
    print()
    print()
    y += 1

# 假设will活100年，每一天他在干什么？
