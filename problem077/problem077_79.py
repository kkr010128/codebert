
def solve():
    a,b,c,d=[int(v) for v in input().split()]
    print(max(a*c, a*d, b*c, b*d))

t = 1 #int(input())
for _ in range(t):
    solve()
