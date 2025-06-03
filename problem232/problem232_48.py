a, b = map(str, input().split())

n1 = a*int(b)
n2 = b*int(a)

ans = n1 if int(n1) > int(n2) else n2

print(ans)