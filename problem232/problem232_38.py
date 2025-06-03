a , b = (int(a) for a in input().split())
x = min(a,b)
t = max(a,b)
ans = [str(x)]*t
print("".join(ans))