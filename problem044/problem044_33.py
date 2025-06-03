# coding=utf-8

a, b, c = map(int, raw_input().rstrip().split())
print sum([1 if not c % i else 0 for i in range(a, b+1)])