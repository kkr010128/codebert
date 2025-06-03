A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())


ans = 'YES' if abs(B - A) <= (V - W) * T else 'NO'
print(ans)
