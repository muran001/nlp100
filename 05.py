#! /user/bin/env python
# _*_ coding: utf-8 _*_

import re

s='I am an NLPer'

def ngram(n,x,d):
    return [d.join(x[i:i+n]).strip(' ') for i in range(len(x)-1)]

print(ngram(2, list(s), ''))
print(ngram(2, [t.strip('.') for t in re.split('[\s,]+', s)], '-'))
