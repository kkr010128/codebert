s = input()
n = int(input())

for i in range(n):
  c = input().split()
  a = int(c[1])
  b = int(c[2])

  if "replace" in c:
    s = s[:a] + c[3] + s[b+1:]
        
  if "reverse" in c:
    u = s[a:b+1]
    s = s[:a] + u[:: -1] +s[b + 1:]

  if "print" in c:
    print(s[a:b+1], sep = '')


