n, r = [int(i) for i in input().split()]
ans = r if n >= 10 else r + 100 *(10 - n)
print(ans)