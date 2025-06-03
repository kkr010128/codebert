n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = []
for s in S:
  for t in T:
    if s == t and not s in C: C.append(s)
print(len(C))