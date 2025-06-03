x, y = map(int,input().split())
money = 0
def yy(money):
    if y == 1:
        money += 300000
    elif y ==2:
        money += 200000
    elif y==3:
        money += 100000
    else:
        money +=0
    print(money)

if x==1 and y==1:
    print(300000*2+400000)
else:
    if x == 1:
        money += 300000
        yy(money)
    elif x ==2:
        money += 200000
        yy(money)
    elif x ==3:
        money += 100000
        yy(money)
    else:
        money +=0
        yy(money)