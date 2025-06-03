n = int(input())
S = []
T = []
for _ in range(n):
  s, t = input().split()
  S.append(s)
  T.append(int(t))
x = input()
index = S.index(x)
if index == n - 1:
  print(0)
else:
  print(sum(T[index+1:]))
