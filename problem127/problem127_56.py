x,y = map(int,input().split())

def solve(x,y):
    legs = x * 2
    while(legs <= x * 4):
        if legs == y:
            print('Yes')
            return
        legs += 2
    print('No')
    return

solve(x,y)