a,b = map(int,input().split())
ans = b if a >= 10 else b + 100 * (10-a)
print(ans)