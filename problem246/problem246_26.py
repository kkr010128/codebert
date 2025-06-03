from itertools import permutations as p

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

j = 0

for i in p(range(1, N + 1)):
  j += 1
  if i == P: a = j
  if i == Q: b = j

if a - b >= 0: print(a - b)
else: print(b - a)  