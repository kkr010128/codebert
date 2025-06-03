import sys
n, m = map(int, input().split())
s = input()
p = n
hist = []
while p>0:
  for i in range(max(0,p-m), p):
    if s[i]=='0':
      hist.append(p-i)
      p = i
      break
  else:
    print(-1)
    sys.exit()
print(*hist[::-1])