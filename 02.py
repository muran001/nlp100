#! /user/bin/env python
# _*_ coding: utf-8 _*_

S='パトカー'
T='タクシー'

r=''.join([s+t for s,t in zip(S,T)])
print(r)
