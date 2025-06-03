import sys

def solve():
    while True:
        x,y = map(int,input().split())
        if x == 0 and y == 0:
            break
        else:
            if x > y:
                x,y = y,x
            print(x,y)
    
solve()
