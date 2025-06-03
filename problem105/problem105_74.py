n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for a0 in a[::2]:
    if a0%2 == 1:
        cnt += 1
print(cnt)