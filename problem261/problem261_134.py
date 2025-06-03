Ss = input().rstrip()

lenS = len(Ss)

ans = 0
for S, T in zip(Ss[:lenS//2], Ss[::-1]):
    ans += S != T

print(ans)
