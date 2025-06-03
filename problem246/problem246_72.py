import itertools

n = int(input())
s = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))
hoge = list(itertools.permutations(range(1, n+1)))
p = 0
q = 0
for i in range(len(hoge)):
  if list(hoge[i]) == s:
    p = i
  if list(hoge[i]) == t:
    q = i
print(abs(p - q))