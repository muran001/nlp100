#! /user/bin/env python
# _*_ coding: utf-8 _*_

import re
s='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
a=[len(t.strip('.')) for t in re.split('[\s,]+', s)]
print(a)
