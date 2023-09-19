# -*- coding: utf-8 -*-
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x * y,L)
def char2num(s):
    if s.isdigit():
        return int(s)
    elif s == ".":
        return 0
    else:
        raise ValueError("Invalid character in string: '{}'".format(s))
def str2float(s):
    pos = s.index(".")
    s = s[:pos] + s[pos+1:]
    return reduce(lambda x,y:x * 10 + y,map(char2num,s)) / (10 ** (len(s) - pos))
