# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/26 20:31
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：类
"""


# 定义一个类
class Dog:
    """
    狗类
    """
    # 类变量定义在类中且在函数体之外。
    dog_type = "中华田园犬"

    def __init__(self, n):
        """
        构造函数，用来创建对象的
        每个类都有构造方法。如果没有显式地定义构造方法，
        在运行的时候将会为该类提供一个默认构造方法
        在创建一个对象的时候，如果有自己写了构造函数，则必须按写的构造函数调用。
        （构造函数只能有一个）
        """
        # 在构造函数中，使用self定义的变量，我们称为实例变量
        # 规范：实例变量尽量在实例和实例函数中使用
        self.name = n
        print('创建狗，名字：' + n)

    def bark(self, s):
        """
        self是实例本身
        是Python语法关键字，代表把你创建的实例传递进函数
        实例函数：第一个参数必须是self。但是在调用的时候，不用传
        规范：实例函数使用对象调用

        实现狗叫的功能
        :return:
        """
        print(self.name + "叫：" + str(s))

    def bark1(self):
        print(self.name)

    @classmethod
    def dog_self(cls, t):
        """
        类函数
        第一个参数必须是cls。调用的时候不传，因为它传的是类本身
        规范：类函数使用类调用
        :return:
        """
        cls.dog_type = t
        print("类函数")


class ADog:
    """
    美国的狗
    """
    # 类变量定义在类中且在函数体之外。
    dog_type = "美国牧羊犬"

    def __init__(self):
        self.n = '小灰'
        print('创建狗，名字：' + self.n)

    def sheep(self):
        """
        圈羊
        :return:
        """
        print(self.n + "在" + "圈羊")
        self.__myname()

    def __myname(self):
        """
        这是私有函数
        只允许类本身使用，类里面使用

        :return:
        """
        print('私有函数')


class ZDog(Dog, ADog):
    """
    子类，继承Dog类
    """

    def __init__(self, n):
        """必须调用所有父类的构造函数"""
        Dog.__init__(self, n)
        ADog.__init__(self)

    def bark(self):
        """
        重写父类的方法，它和参数列表无关
        :param s:
        :return:
        """
        print(self.name + "在叫")

    def eat(self):
        """
        拓展，拓展实现没有实现过的功能
        :return:
        """
        print(self.name + '在啃骨头')
