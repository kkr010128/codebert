n, k = map(int,input().split())
lst = list(map(int,input().split()))
lst2 = sorted(lst)
ans = 0
for i in range(k):
  ans = ans + lst2[i]
print(ans)