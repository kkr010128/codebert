X,K,D = map(int,input().split())
X = abs(X)
ans = 0

if (X // D) >= K:
    ans = X - (K * D)
elif (X // D) % 2 == 0:
    if K % 2 == 0:
        ans = X % D
    else:
        ans = abs((X % D) - D)
else:
    if K % 2 ==1:
        ans = X % D
    else:
        ans = abs((X % D) - D)

print(ans)