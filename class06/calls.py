# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/26 20:32
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：调用类
"""
# 调用狗类，创建一条狗，并且叫两声
from class06.example02 import Dog, ZDog, ADog

# # # 创建一个类的对象
# # # 和类名一样的函数，是调用构造函数
# dog = Dog('小黑')
#
# # # 调用实例函数
# # dog.bark("旺旺旺")
# # dog.bark1()
#
# # 调用类函数
# Dog.dog_self('中华田园犬')
#
# dog2 = Dog('小白')
# print(Dog.dog_type)


# zdog = ZDog('小黑')
# # 重写
# zdog.bark()
# # 继承
# zdog.sheep()
# # 拓展
# zdog.eat()
# print(ZDog.dog_type)


# 基础函数和基础变量
# 基础变量：代表类最开始的描述的段落文字
# print(Dog.__doc__)
# dog = Dog('小白')
# print(dog.bark.__doc__)
#
# print(dog.__str__())
# print(dog.__dict__)


from class06.example04 import MyGlobal


myglobal = MyGlobal()
myglobal.func_2()






