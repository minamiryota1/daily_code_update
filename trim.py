#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def trim(s):
    a0 = -len(s) - 1
    a = a0
    b = a0
    for i in range(len(s)):
        if s[i] != " " and a == a0:
            a = i
        if s[-i-1] != " " and b == a0:
            b = len(s)-i
        if a != -len(s)-1 and b != -len(s)-1:
            break
    s = s[max(a,0):max(0,b)] 
    return s
if trim('hello  ') != 'hello':
    print('测试失败!1' + trim('hello  ')) 
elif trim('  hello') != 'hello':
    print('测试失败2!' + trim('  hello'))
elif trim('  hello  ') != 'hello':
    print('测试失败3!' + trim('  hello  '))
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4' + trim('  hello  world  '))
elif trim('') != '':
    print('测试失败!5' + trim(''))
elif trim('    ') != '':
    print('测试失败!6' + trim('    '))
else:
    print('测试成功!')
