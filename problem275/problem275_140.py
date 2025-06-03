X, Y = map(int, input().split())

def solver(X, Y):
    if X == 1 and Y == 1:
        print(1000000)
        return
    
    a = 0
    if X == 1:
        a += 300000
    if X == 2:
        a += 200000
    if X == 3:
        a += 100000
    if Y == 1:
        a += 300000
    if Y == 2:
        a += 200000
    if Y == 3:
        a += 100000
    
    print(a)

solver(X, Y)