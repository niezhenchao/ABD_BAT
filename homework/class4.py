# -*- coding: UTF-8 -*-

# # 选择排序
# height = [155, 187, 172, 160, 163, 166, 173, 182, 165, 159]
# # 外层循环代表轮次
# l = len(height)
# i = 0
# while i < l - 1:
#     # 内层循环，选择最大的
#     # 以第一个人为基准，记录下标
#     j = 1
#     tmp = 0
#     while j < l - i:
#         if height[tmp] < height[j]:
#             # 记录最大值下标
#             tmp = j
#         j = j + 1
#     # # 把最高的放到最后
#     t = height[tmp]
#     height[tmp] = height[l - i - 1]
#     height[l - i - 1] = t
#     i += 1
#     # 交换
#     # height[tmp], height[len(height) - i - 1] = height[len(height) - i - 1], height[tmp]
#
# print(height)
#
# # 冒泡排序
# height = [190, 187, 172, 160, 163, 166, 173, 182, 165, 159]
#
# # 外层循环：控制比较的轮数
# i = 0
# # 要不要-1？需要-1，因为最后一轮只剩一个数，不用比较
# while i<len(height)-1:
#     # j从几开始？和前一个比，就从1开始，如果和后一个比就从0开始
#     j = 0
#     # 内存循环：每一轮的比较
#     # 注意：-i可以提升效率，减少比较的次数。因为每一轮比较后，已经冒出来的元素是不用再比较的
#     # 而这个冒出来的元素都放到了列表的最后
#     while j<len(height)-1-i:
#         # 和前一个比较，如果比后一个大就交换
#         if height[j] < height[j+1]:
#             # 前一个和后一个交换
#             height[j],height[j+1] = height[j+1],height[j]
#
#         # 循环控制条件
#         j += 1
#
#     # 循环控制条件
#     i += 1
#
# print(height)

# 杨辉三角
# l1用来存储上一行的系数
l1 = [1]
# l2用来存储下一行的系数
l2 = [1, 1]
# yh用来存储杨辉三角的次数
yh = int(input("请输入杨辉的次方:"))

# 定义变量控制输出位数
len_out = 4

# 控制杨辉的次方
i = 0
while i < yh + 1:
    # 直接输出当前行
    # 前面输出多少位呢？
    print("%*s" % (len_out // 2 * (yh - i), ''), end='')

    for ii in range(i + 1):
        print("%*s" % (len_out, l1[ii]), end='')
    print()
    # 通过循环得到下一行
    j = 0
    while j < i + 2:
        # 判断是第一个或者最后一个，它的值就是1
        if j == 0 or j == i + 1:
            l2[j] = 1
        else:
            # 不是边界的时候
            l2[j] = l1[j - 1] + l1[j]

        j += 1

    i += 1
    # 复制l2的元素到l1，l2就变成了上一行
    l1 = l2
    # l2将要存储的下一行，多一个系数
    l2 = l1 + [1]
