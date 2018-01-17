#! /usr/bin/env python3

import operator


class numstr(object):
    '''数字与字符串结合的一个测试类，重载了几个常用符号'''

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__str = string

    def __str__(self):
        return '[{0}::{1}]'.format(self.__num, self.__str)

    def __add__(self, other):
        if isinstance(other, numstr):
            return self.__class__(self.__num + other.__num, self.__str + other.__str)

        else:
            raise TypeError("参数错误")
    # 重载乘法

    def __mul__(self, num):
        if isinstance(num, numstr):
            return self.__class__(self.__num * num, self.__str * num)
        else:
            raise TypeError("参数错误")
    # 判断是否为空

    def __nonzero__(self):
        return self.__num or self.__str

    def __norm_cval(self, cmpers):
        return operator.eq(cmpers, 0)

    def __cmp__(self, other):
        return self.__norm_cval(operator.eq(self.__num, other.__num)) + self.__norm_cval(operator.eq(self.__str, other.__str))
