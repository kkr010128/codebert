n, x, t = map(int, input().split())
nt = (n + x - 1) / x 
ans = int(nt) * t
print(ans)