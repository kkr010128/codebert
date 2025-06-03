n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    m = max(a)
    b = sum([i**2 for i in a if i != m])
    if (m**2 == b):
        print("YES")
    else:
        print("NO")