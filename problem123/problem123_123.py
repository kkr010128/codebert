n = int(input())
a = list(map(int,input().split()))

t=0
for i in a:
  t = t ^ i
ans = []
for i in a:
  ans.append(t ^ i)
print(" ".join(str(i) for i in ans))