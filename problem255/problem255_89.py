N = int(input())
S,T = map(str, input().split())
s=[]
for i in S:
    s.append(i)
t=[]
for i in T:
    t.append(i)
for i in range(N):
  print(s[i]+t[i], end="")
