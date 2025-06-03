n,m = map(int,input().split())
if n % 2 == 1:ans = [[1+i,n-i] for i in range(n//2)]
else:ans = [[1+i,n-i] for i in range(n//4)]+[[n//2+1+i,n//2-1-i] for i in range(n//2-n//4-1)]
for i in range(m):print(ans[i][0],ans[i][1])