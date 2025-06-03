N = int(input())
a = list(map(int, input().split()))
ans = 0

i = 1
for num in a:
    if num != i:
        ans += 1
    else:
        i += 1

print(ans if ans < len(a) else -1)