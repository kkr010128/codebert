n = int(input())
a = list(map(int,input().split()))
ans = [0]*(n+1)
a.insert(0,0)
for i in range(1,n+1):
	ans[a[i]] += i
ans.pop(0)
ans = [str(ans[s]) for s in range(n)]
print(" ".join(ans))