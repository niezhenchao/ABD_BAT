# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/14 21:17
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：数据类型的要点
"""
# 转义：\  (把有特殊含义的符号转成普通符号，使它失去特殊含义)
# 你要在字符串里面出现单引号和双引号怎么办？
s = "'''''''''''''"
print(s)
s = "\""
print(s)
# 转义字符:(把无特殊含义的符号转成有特殊含义的符号，使它具备符合规则的特殊含义)
print("a\ta\na")

# 类型的互斥：数字和其他类型的互斥，NoneType和所有类型互斥
i = 1
f = 1.1
s = 'aa'
# 布尔类型的本质是数字：True=1, False=0
b = True
n = None
print(i + f)
print(i + b)
# print(s+n)

# 强转：所有类型都可以强转为字符，字符串转其他类型，必须要符合其他类型的写法
print(str(i) + s)

s = '1'
print(i + float(s))
print(str(None) + s)
