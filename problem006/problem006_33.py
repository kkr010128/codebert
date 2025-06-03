#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

result = 100000
num = int(raw_input())

for i in range(num):
	result *= 1.05
	result /= 1000
	result = math.ceil(result)
	result *= 1000

print int(result)