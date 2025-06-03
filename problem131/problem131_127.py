# B - Tag

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

ans = 'NO'
dist = abs(A - B)
diff = V - W

if diff > 0 and dist <= T * diff:
    ans = 'YES'
print(ans)

