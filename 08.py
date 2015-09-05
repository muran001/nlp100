#! /user/bin/env python
# _*_ coding: utf-8 _*_

def cipher(t):
    return ''.join([chr(219-ord(u)) if u.islower() else u for u in list(t)])

s='ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day.'

print('before:')
print(s)
print('encrypted:')
print(cipher(s))
print('decrypted:')
print(cipher(cipher(s)))
