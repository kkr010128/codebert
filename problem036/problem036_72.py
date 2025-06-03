# coding: utf-8

input_nums = raw_input().rstrip().split()
a, b = [int(x) for x in input_nums]
menseki = a * b
syutyo = 2 * (a + b)
print menseki, syutyo