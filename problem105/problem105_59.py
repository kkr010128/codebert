N = int(input())
a = list(map(int, input().split()))

ans = 0

for index, item in enumerate(a):
    if (index+1) % 2 != 0 and item % 2 != 0:
        ans += 1

print(ans)
