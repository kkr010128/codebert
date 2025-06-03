import itertools
 
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
 
# Nが10程度で小さい
# 階乗の全探索をしても間に合う
# Pythonならitertoolsが使える
# permutations（関数）にlistを渡すと、順列を生成！
l = [i for i in range(1, N+1)]
permutations_l = list(itertools.permutations(l))

a, b = 0, 0
for i, R in enumerate(permutations_l):
  if R == P: a = i
for i, R in enumerate(permutations_l):
  if R == Q: b = i

print(abs(a-b))