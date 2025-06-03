N = int(input())
S = input()

A = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ans = ''
for s in S:
  ans += A[(A.index(s)+N)%26]

print(ans)