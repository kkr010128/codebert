n = int(input())

a = list(map(int, input().split()))

target = 1

broken = 0

for i in a:
    if i == target:
        target += 1
    else:
        broken += 1

if broken < n:
    print(broken)
else:
    print(-1)