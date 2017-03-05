# -*- coding:utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
        # array 二维列表
        def Find(self, target, array):
            if len(array) < 1:
                return False
            # write code here
            for i,value in enumerate(array):
                if len(value) < 1:
                    return False
                if value[0] == target or (value[0] < target and target in value):
                    return True
        return False

