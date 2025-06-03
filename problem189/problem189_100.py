nm = input().split()
n = int(nm[0])
m = int(nm[1])

ans = 0

n1 = n*(n-1)/2

n2 = m*(m-1)/2

ans = int(n1 + n2)

print(ans)