# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 21:08
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：元组
"""
# 元组的定义
tup1 = ()
# 如果是只有一个元素的元组
tup2 = (1,)
print(type(tup2))
tup3 = (1, 2, 3, '4')
# tup3[3] = 4
# print(tup3)

# 元素可以相加
tup3 = tup2 + tup3
print(tup3)


# 成员遍历
for item in tup3:
    print(item)

print('###################')
# 下标遍历
for i in range(len(tup3)):
    print(tup3[i])
