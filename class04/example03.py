# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/21 20:40
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：冒泡排序
"""
"""
全班学生身高
height = [166, 187, 156, 144, 155, 177, 167, 153, 188, 169]
从低到高排序
"""
"""
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误
就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。用循环嵌套实现排序
"""
height = [166, 187, 156, 144, 155, 177, 167, 153, 188, 169]

# 冒泡的轮次
for j in range(0, len(height) - 1):
    # 冒出最大的来
    for i in range(1, len(height) - j):
        # 如果前面一个比后面一个大，就交换位置
        if height[i - 1] > height[i]:
            height[i - 1], height[i] = height[i], height[i - 1]

print(height)
