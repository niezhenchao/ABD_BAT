# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 21:21
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：字典
"""
# 字典：特斯汀学院老师的身高
# 键值对格式的数据结构：key:value，key是不能重复
dict1 = {}
dict2 = {'will': 190, 'roy': 180, 'tufei': 170, 'kaka': '160'}
# 获取键的值
print(dict2.get('kaka'))
print(dict2['kaka'])

# 更新
dict2['will'] = 185
print(dict2)

# # 清空
# dict2.clear()
# print(dict2)

# 删除
# dict2.pop('kaka')
del dict2['kaka']
print(dict2)

# 新增
dict2['kaka'] = 185
print(dict2)

# 合并
dict3 = {'youmi': 166, 'will': 188}
dict3.update(dict2)
print(dict3)


