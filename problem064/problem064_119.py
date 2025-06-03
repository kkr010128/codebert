# coding: utf-8
ring = input()
pattern = input()

ring *= 2

if pattern in ring:
    print('Yes')
else:
    print('No')