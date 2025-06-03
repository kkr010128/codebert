N = input()
A = list(map(int,input().strip().split()))

ans = 0
for i in range(len(A)):
    if i%2==0 and A[i]%2==1:
        ans += 1
print(ans)