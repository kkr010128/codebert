X, K, D = map(int, input().split())
ans = abs(abs(X) - D*K)

a = abs(X)//D
b = abs(X)%D
if (K - a)%2 == 1 and a < K:
    ans = D - b
elif (K - a)%2 == 0 and a < K:
    ans = b

print(ans)