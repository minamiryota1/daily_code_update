#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None,None)
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min,max)
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')
