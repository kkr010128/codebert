#DISCO presents ディスカバリーチャンネル コードコンテス a
def get_money(num):
    if num==3:
        return 100000
    elif num==2:
        return 200000
    elif num==1:
        return 300000
    else:
        return 0
x,y=map(int,input().split())
money=get_money(x)+get_money(y)
if x==y and x==1:
    money+=400000
print(money)