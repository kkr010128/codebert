x,k,d = map(int,input().split())
check = []
if abs(x) // d > k :
    print(abs(abs(x)- k*d))
else:
    if (k - x//d) % 2 == 0:
        print(abs(x - d*(x//d)))
    else:
        print(min(abs(x - d*(x//d - 1)), abs(x - d*(x//d + 1))))
