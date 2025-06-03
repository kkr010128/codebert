ans = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a == 2:
        ans += 1
    elif a%2 == 0:
        continue
    else:
        if pow(2, a-1, a) == 1:
            ans += 1

print(ans)