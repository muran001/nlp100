#! /user/bin/env python
# _*_ coding: utf-8 _*_

import random, re

def shuffle_middle(t):
    if len(t) < 4: return t
    u = list(t[1:-1])
    random.shuffle(u)
    return ''.join([t[:1]]+u+[t[-1:]])

s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print('before'); print(s)
r=' '.join([shuffle_middle(x) for x in re.split('[\s]+', s)])
print('after'); print(r)
