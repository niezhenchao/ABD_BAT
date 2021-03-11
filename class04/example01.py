# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/21 20:21
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：简单算法
"""
"""
算法1：把字符串'a,b,c,d,e,f,g,h,i,j,k,l'，变成一个字符列表，不需要逗号
算法分析：通过遍历，我们取出每一个字符，然后不要逗号，存放到列表
"""
s = 'a,b,c,d,e,f,g,h,i,j,k,l'
# 通过遍历，取出每一个字符
slist = []
for ss in s:
    # 如果是逗号就不要它
    if ss == ',':
        pass
    else:
        slist.append(ss)

print(slist)
# 沿着某一个特定的字符，把一个字符串切割成子字符串列表，这个特定字符会被抛弃
print(s.split(','))

"""
算法2：'Will is young, Will is handsome'
    需要把里面的Will换成Roy
算法解析：直接把Will全部替换为Roy
"""
# 替换
s = 'Will is young, Will is handsome, Will is '
s1 = s.replace('Will', 'Roy', 1)
print(s1)
# 替换第二个
s1 = s.replace('Will', 'Roy', 2)
s1 = s1.replace('Roy', 'Will', 1)
print(s1)
# 替换最后一个
s1 = s[::-1]
s1 = s1.replace('lliW','iefut',1)
s1 = s1[::-1]
print(s1)
