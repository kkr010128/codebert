a,b = input().split()
ans = sorted( [a*int(b),b*int(a)] )[0]
print(ans)