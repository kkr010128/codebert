a, b = map(float, input().split())
a = int(a)
b_int = int(b*100)

ans = a*b_int/100
ans = int(ans)
print(ans)