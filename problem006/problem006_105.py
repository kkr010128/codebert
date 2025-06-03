week=int(input())
money=100000
for i in range(week):
    money=money*1.05
    if money%1000!=0:
        money=1000*(money//1000+1)

print(int(money))