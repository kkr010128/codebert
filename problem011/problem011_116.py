x, y = [int(i) for i in input().split()]

if x < y:
    a = x
    x = y
    y = a

def kouyakusu(x,y):
    yakusu = x % y
    if yakusu == 0:
        print(y)
        return y
    else:
        kouyakusu(y,yakusu)

max_kouyakusu = kouyakusu(x,y)