# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/21 20:40
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：选择排序
"""
"""
全班学生身高
height = [166, 187, 156, 144, 155, 177, 167, 153, 188, 169]
1.找出最高的学生身高
2.从低到高排序
"""
height = [166, 187, 156, 144, 155, 177, 167, 153, 188, 169]

maxh = height[0]
for i in range(1, len(height)):
    if height[i] > maxh:
        maxh = height[i]

print(maxh)

"""
每一次从待排序的数据元素中选出最小（或最大）的一个元素，
存放在序列的起始位置或者结束为止，直到全部待排序的数据元素排完。
"""
height = [166, 187, 156, 144, 155, 177, 167, 153, 188, 169]

# 控制比较和交换的轮次
for j in range(0, len(height) - 1):
    # 记录最大的下标
    maxh = 0
    for i in range(1, len(height) - j):
        if height[i] > height[maxh]:
            # 记录大的下标
            maxh = i

    # 把最大的和最后一做对调
    height[maxh], height[len(height) - 1 - j] = \
        height[len(height) - 1 - j], height[maxh]

print(height)

a = 1
b = 2
a, b = b, a
print(a, b)
