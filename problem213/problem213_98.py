n = int(input())

x = list(map(int, input().split()))

ans = 10**6

for i in range(1, 101):
    str = 0
    for j in x:
        str += (j-i)**2
    ans = min(ans, str)

print(ans)