#! -*- coding: utf-8 -*-

import random
import math

s = input()
nums = len(s) - 3
index = math.floor(random.random() * nums)

print(s[index: index + 3])
