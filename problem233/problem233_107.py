N = int(input())
P = list(map(int,input().split()))
a = 0
s = 10**6

for p in P:
  if p<s:
    a+=1
    s=p

print(a)