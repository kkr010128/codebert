n = int(input())
A = list(map(int,input().split()))
ans = 0 
t = 0
for e,(i , j) in enumerate(zip(A,A[1:])):
    if i + t > j : 
        ans += t + i-j
        t= t + i-j
    else:t = 0
    # print(t,ans)
print(ans)