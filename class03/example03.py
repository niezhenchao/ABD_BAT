# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 20:37
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：列表的遍历
"""
# 列表的定义
height1 = ['will', 'roy', 'tufei', 'kaka']
height2 = [190, 180, 170, 160]

# 列表的遍历：把里面每一个元素都经历一遍
for i in range(len(height2)):
    height2[i] += 2

print(height2)

# 成员遍历
# 只适合读取里面的内容，不能修改
for item in height2:
    print(item)
    item += 2

print(height2)
