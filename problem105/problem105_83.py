N = int(input())
a = list(map(int, input().split()))
cnt = 0
i = 1
while i <= N:
    if a[i-1] % 2 == 1:
        cnt += 1
    i += 2
print(cnt)