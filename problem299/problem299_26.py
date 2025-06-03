n=int(input())
a=list(map(int,input().split()))
ans=[x for x in range(n)]
for i in range(n):
  ans[(a[i] - 1)] = i + 1
for aaa in ans:
  print(aaa)