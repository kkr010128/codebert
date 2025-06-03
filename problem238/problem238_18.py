n,k,s = map(int,input().split())

if s == 10**9:
    ans = [1]*n
    for i in range(k):
        ans [i] = s
else:
    ans = [s+1]*n
    for i in range(k):
        ans[i] = s

for i in ans:
    print(i,end = " ")
