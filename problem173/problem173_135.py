N = int(input())
ans = 0
for n in range(1, N+1):
    if n % 3 == 0 and n % 5 == 0:
        pass
    elif n % 3 == 0:
        pass
    elif n % 5 == 0:
        pass
    else:
        ans += n % (10**9+7)
print(ans)