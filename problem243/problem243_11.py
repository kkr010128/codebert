N = int(input())
P = [input().split() for i in range(N)]
M = input()

chk = 0
value = 0
for i, (k, v) in enumerate(P):
  if k == M:
    chk = int(v)
  elif chk != 0:
    value += int(v)

print(value)