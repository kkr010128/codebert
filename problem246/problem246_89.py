import itertools

n=[x for x in range(1,int(input())+1)]
P=list(map(int, input().split()))
Q=list(map(int, input().split()))

for i, a in enumerate(itertools.permutations(n), start=1):
  if list(a)==P:
    p=i
  if list(a)==Q:
    q=i
print(abs(p-q))
