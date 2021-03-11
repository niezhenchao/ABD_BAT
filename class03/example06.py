# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 21:38
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：字典的遍历
"""
height = {'youmi': 166, 'will': 185, 'roy': 180, 'tufei': 170, 'kaka': 185}

# 需把每个人身高都减1

# # 键的遍历
# for key in height.keys():
#     height[key] += 1
#     print(height[key])

# # 值的遍历：不能修改内容
# for value in height.values():
#     print(value)

# 键值对的遍历
for item in height.items():
    print(item)

for key,value in height.items():
    print(','.join((key,str(value))))

