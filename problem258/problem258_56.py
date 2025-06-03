N = int(input())
if N % 2 == 1:
    print(0)
    exit()

ans = 0
N //= 2
i = 1
while N >= 5 ** i:
    ans += (N // 5 ** i)
    i += 1

print(ans)
