#! /user/bin/env python
# _*_ coding: utf-8 _*_

import re

s='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

def trim(i, x):
    return (i, x[:1:] if i in [1,5,6,7,8,9,15,16,19] else x[:2:])

r=dict([trim(i+1, x) for i,x in enumerate(re.split('[\s,]', s))])
print(r)
