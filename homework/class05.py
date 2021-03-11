# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/4 20:16
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：字符串处理
"""


def reserve_str(s):
    """
    字符串反转
    :param s: 需要反转的字符串
    :return:
    """
    return s[::-1]


def get_same_of_str(s):
    """
    返回字符串相反的两部分
    :param s: 源字符串
    :return: 返回相反的两个字符串
    """
    str1 = reserve_str(s)
    # 只有反转后的字符串，才能返回相反的两部分
    if str1 == s:
        l = len(s)
        if l % 2 == 0 :
            # 偶数长度，直接返回两部分
            return s[0:l//2], s[l//2:]
        else:
            # 奇数长度，最中间的字符前后都要有
            return s[0:l // 2 + 1], s[l // 2:]
    else:
        return None


if __name__ == "__main__":
    # 给一个字符串，判断是否为回文字符串，如果是就返回相反的两部分
    s1 = "abcba"
    print(reserve_str(s1))
    print(get_same_of_str(s1))