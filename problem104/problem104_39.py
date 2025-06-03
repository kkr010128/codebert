l,r,d = map(int, input().split())
if l%d == 0:
    print(r//d - l//d + 1)
else:
    print(r//d - l//d)