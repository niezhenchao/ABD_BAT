# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/23 21:49
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：递归快排
"""
import time


def quick_sort(height, left, right):
    """
    我们每一轮，选取最后一个元素为基准，把元素分成左右两部分，左边都比
    基准小，右边都比基准大。进行如下操作：从左往右找比基准大的，交换到
    h位置， h往左移动一位；再从h位置从右往左找比基准小的，交换到之前l
    的位置，l往右移动一位。反复执行前面的操作，直到l=h，因为这个时候说
    明整个列表的元素都和基准进行了比较。也就达到了基准前面的元素都比基
    准小，基准后面的元素都比基准大。当整个递归执行到列表只有一个元素的
    时候，就可以保证整个列表是有序的。
    :param height: 待排序的列表
    :param left: 待排序元素的左下标
    :param right: 待排序元素的右下标
    :return:
    """
    # 最开始判断出口
    if left >= right:
        return

    # 最开始的时候，l和h分别指向待排序元素的开始和末尾
    l = left
    h = right

    # 取最后一个元素为基准
    base = height[h]

    # 只要l小于h，就说明还没找完，需要继续找
    while l < h:
        # 从左往右找比基准大的
        while l < h:
            # 从左往右找比基准大的，交换到h位置,h往左移动一位；
            if height[l] > base:
                height[l], height[h] = height[h], height[l]
                h -= 1
                break
            else:
                # 如果没找到就继续往右找
                l = l + 1

        # 从h位置从右往左找比基准小的
        while l < h:
            # 从左往右找比基准大的，交换到h位置,h往左移动一位；
            if height[h] < base:
                height[l], height[h] = height[h], height[l]
                l += 1
                break
            else:
                # 如果没找到就继续往左找
                h = h - 1
    # # 左边出口
    # if left >= l - 1:
    #     pass
    # else:
    #     # 递归实现左边的排序
    quick_sort(height, left, l - 1)

    # # 右边出口
    # if right <= h + 1:
    #     pass
    # else:
    #     # 递归实现右边的排序
    quick_sort(height, h + 1, right)


height = [144, 166, 187, 156, 144, 155, 177, 167, 153, 188, 169,144]
quick_sort(height, 0, len(height) - 1)
print(height)

# t1 = time.time()
# time.sleep(1)
# t2 = time.time()
# print(t2-t1)
