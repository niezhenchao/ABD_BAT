# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/21 21:17
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：杨辉三角
"""
"""
算法分析：如果我们知道上一行的系数，就能算出下一行的系数
我们可以从第一行开始推，推N行的系数
"""

# 需要推的杨辉的次方数
yh = 10

# 上一行
arr1 = [1]
print("%*s" % (yh*3,''),end='')
print('%-6d' % 1)

# 这里为什么要yh+1?
# 0次方是已知的
for j in range(1,yh+1):
    # 推算下一行
    # 下一行要比上一行多一个元素
    arr2 = arr1 + [1]

    for i in range(0,len(arr2)):
        if i == 0 or i == j:
            # 最左边，最右边的元素都是1
            arr2[i] = 1
        else:
            # 等于肩膀上两个元素的和
            arr2[i] = arr1[i-1] + arr1[i]

    # 在推算下一次方之前，我们需要把刚推出来的次方系数作为已知系数
    arr1 = arr2
    print('%*s' % ((yh-j)*3,''),end='')
    for i in range(0,len(arr1)):
        print('%-6d' % arr1[i],end='')

    print()

