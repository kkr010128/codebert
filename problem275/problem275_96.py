X,Y = (int(i) for i in input().split())

def get_money(Z):
    if Z == 3:
        return(100000)
    elif Z == 2:
        return(200000)
    elif Z == 1:
        return(300000)
    else:
        return(0)


x = get_money(X)
y = get_money(Y)

if X == 1 and Y == 1:
    z = 400000
else:
    z = 0
ans = x + y + z

print(ans)