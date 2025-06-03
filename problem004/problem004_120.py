n = int(input())
for i in range(0, n):
    a, b, c = sorted(map(int, input().split()))
    print("YES" if c*c == a*a+b*b else "NO")