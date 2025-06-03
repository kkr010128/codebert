def division(x,y):
    if y == 0:
        return x
    return division(y, x%y)

x,y=map(int,input().split())

kotae = division(x,y)
print(kotae)