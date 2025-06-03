def ifTriangle(a, b, c):
    if (a**2) + (b**2) == c**2: print("YES")
    else: print("NO")

n=int(input())
for i in range(n):
    lines=list(map(int, input().split()))
    lines.sort()
    ifTriangle(lines[0], lines[1], lines[2])