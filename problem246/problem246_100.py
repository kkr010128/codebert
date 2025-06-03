# 25
import itertools

n = int(input())
a = tuple(list(map(int,input().split())))
b = tuple(list(map(int,input().split())))
list = [num for num in range(1, n + 1)]

count = 1
aidx = bidx = 0
for i in itertools.permutations(list, n):
    if i == a: aidx = count
    if i == b: bidx = count
    if aidx != 0 and bidx != 0: break
    count += 1

print(abs(aidx - bidx))