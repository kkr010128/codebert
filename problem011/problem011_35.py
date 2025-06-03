x,y = map(int,input().split(" "))

def gdp(x,y):
    if x > y:
        big = x
        small = y
    else:
        big = y
        small = x
    if big%small == 0:
        print(small)
        return
    else:
        gdp(small,big%small)

gdp(x,y)

