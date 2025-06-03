N = int(input())
if N % 2 == 1:
    print(0)
    exit()
ans = 0
i = 1
while 5 ** i * 2 <= N:
    ans += N // (5 ** i * 2)
    i += 1
print(ans)
