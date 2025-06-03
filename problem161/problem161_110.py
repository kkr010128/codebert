A, B, N = map(int, input().split())

val = min(B-1, N)
ans = (A*val/B/1.0)//1
print(int(ans))
