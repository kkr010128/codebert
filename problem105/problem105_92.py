# coding: utf-8

n = int(input())
a_array = list(map(int, input().split()))

count = 0
for i, a in enumerate(a_array):
    if i % 2 == 0 and a % 2 != 0:
        count += 1
        
print(count)
