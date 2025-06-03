L, R, d = map(int, input().split())

if L%d == 0 or R%d == 0 :
    print((R-L)//d + 1)
else:
    print((R - L)//d)