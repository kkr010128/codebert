n = int(input())

ls = []
rs = []
for _ in range(n):
    x, y = map(int, input().split())
    ls.append(x)
    rs.append(y)

ls = sorted(ls)
rs = sorted(rs)

if n % 2 == 1:
    print(rs[len(rs)//2] - ls[len(ls)//2] + 1)
else:
    a = (rs[len(rs)//2-1] * 10 + rs[len(rs)//2] * 10) // 2
    b = (ls[len(ls)//2-1] * 10 + ls[len(ls)//2] * 10) // 2
    print((a - b) // 5 + 1)