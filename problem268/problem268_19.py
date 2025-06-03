n = int(input())
a = list(map(int, input().split()))

status = [0, 0, 0]
mod = 1000000007

ans = status.count(a[0])
status[0] += 1

for i in range(1, n):
    ans *= status.count(a[i])
    ans %= mod

    for j in range(len(status)):
        if status[j] == a[i]:
            status[j] += 1
            break

print(ans)

