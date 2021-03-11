# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/16 21:04
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：for循环
"""
# 每个月上半个月每天我们都上java，下半个月每天我们都上Python
# 需求：打印每个月每一天我在干什么

# 先以10月为例
# 每个月从1号开始
# 左闭右开区间[1,31)：1<=i<31
# 第三个参数叫步长：每循环一次自增多少，默认是1
for i in range(1, 32):
    if i <= 15:
        print(str(i) + '号上java课')
    else:
        print(str(i) + '号上python课')

# 打印今年每一天will在干什么
for j in range(1, 13):
    print(j)
    # 确定每个月的天数
    # 二月份：
    if j == 2:
        days = 29
    else:
        # 31天的有哪些情况？
        # y<=7的时候的奇数，和y>=8的偶数
        if (j <= 7 and (j % 2) == 1) or (j >= 8 and (j % 2) == 0):
            days = 31
        else:
            days = 30

    for i in range(1, days + 1):
        # 要比较334次
        if j == 10:
            break
        if i <= 15:
            print(str(i) + '号上java课', end='；')
        else:
            print(str(i) + '号上python课', end='；')

    print()
    print()

# 假设will活100年，每一天他在干什么？
"""
课外作业
"""

# # 字符串遍历
# s = 'abcdefghijklmn'
# for ss in s:
#     print(ss)
