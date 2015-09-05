#! /user/bin/env python
# _*_ coding: utf-8 _*_

import re

s='paraparaparadise'
t='paragraph'

def ngram(n,x,d):
    return [d.join(x[i:i+n]).strip(' ') for i in range(len(x)-1)]

sb=ngram(2, list(s), '')
tb=ngram(2, list(t), '')
print('sb=', end=''); print(sb)
print('tb=', end=''); print(tb)
sum_sbtb=list(set(sb) & set(tb))
diff_sbtb=list(set(sb) - set(tb))

print('sum=', end=''); print(sum_sbtb)
print('diff=', end=''); print(diff_sbtb)
