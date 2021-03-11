# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/4 10:35
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：三大排序算法
"""
import sys
import time


def bubble_sort(height):
    """
    冒泡排序
    :param height: 待排序列表
    :return: 排序后列表
    """
    # 最外层控制比较的轮次
    for j in range(0, len(height) - 1):
        # 内层循环控制交换
        # 为什么从1开始？下标为0的人，没有可以比的
        for i in range(1, len(height) - j):
            # 如果后一个比前一个小，就交换
            if height[i] < height[i - 1]:
                height[i], height[i - 1] = height[i - 1], height[i]

    return height


def select_sort(height):
    """
    选择排序
    :param height: 待排序列表
    :return: 排序后列表
    """
    # 外层循环，选择多少个人出来
    for j in range(0, len(height) - 1):
        # 记录最高的人的下标
        m_h = 0
        # 内层循环，从剩下的人里面选出最高的
        for i in range(1, len(height) - j):
            if height[m_h] < height[i]:
                m_h = i

        # 选出最高的之后，把他排到待选人的最后
        height[m_h], height[len(height) - j - 1] = height[len(height) - j - 1], height[m_h]

    return height


def quick_sort(heigth, left, right):
    l = left
    h = right

    # 选择最后一个为基准
    base = heigth[h]

    while l < h:
        while l < h:
            # 从左往右找比基准大的
            if heigth[l] > base:
                heigth[l], heigth[h] = heigth[h], heigth[l]
                # h往左移动一位
                h = h - 1
                break
            else:
                l = l + 1

        while l < h:
            # 从右往左找比基准小的
            if heigth[h] < base:
                heigth[l], heigth[h] = heigth[h], heigth[l]
                # l往右移动一位
                l = l + 1
                break
            else:
                h = h - 1

    if l > left + 1:
        # 对左边继续排序
        quick_sort(heigth, left, l - 1)

    if h < right - 1:
        # 对右边继续排序
        quick_sort(heigth, h + 1, right)


if __name__ == '__main__':
    # 修改堆栈大小的限制
    sys.setrecursionlimit(100000)

    # 初始化倒序列表
    list1 = [i for i in range(3000, 0, -1)]
    print(str(list1))
    t1 = time.time()
    bubble_sort(list1)
    print(list1)
    print("###冒泡排序的时间：" + str(time.time()-t1))


    # 初始化倒序列表
    list1 = [i for i in range(3000, 0, -1)]
    print(str(list1))
    t1 = time.time()
    select_sort(list1)
    print(list1)
    print("###选择排序的时间：" + str(time.time()-t1))

    # 初始化倒序列表
    list1 = [i for i in range(3000, 0, -1)]
    print(str(list1))
    t1 = time.time()
    quick_sort(list1,0,len(list1)-1)
    print(list1)
    print("###选择排序的时间：" + str(time.time() - t1))

