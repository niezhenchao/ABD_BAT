# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 20:37
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：列表
"""
# 列表的定义
height1 = []
height2 = [190, 180, 170, 160]

# 列表的使用
# 获取元素的值
"""
下标：index，从0开始的整数
[190, 180, 170, 160]
[0, 1, 2, 3]
"""
print(height2[0])

# 修改
height2[0] = 181
print(height2)

# 新增：在末尾新增，在指定位置新增
height2.append(180)
print(height2)
height2.insert(2, '166')
print(height2)

# 删除：按值删除，按下标删除
height2.remove(180)
print(height2)
del height2[1]
print(height2)

# 加法：合并
height1 = ['a', 'b', 'c']
height3 = height1 + height2
print(height3)

# 截取[x:y]：左闭右开[x,y)
print(height3[1:4])

# 如果下标是负数，就是反向截取，负数是(-x,y]，0不需要写
print(height3[-4:])

# x或者y缺失的情况
print(height3[:5])
print(height3[1:])

# 反向
print(height3[::-1])

# 字符串的拓展，字符是可以直接作为一个字符列表使用的
s = 'Will'
s = s[::-1]
print(s)
