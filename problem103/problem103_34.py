n = int(input())
a = input().split()

money = 1000
stock = 0
pivot = []
upflag = 0
dnflag = 1

if(int(a[1]) - int(a[0]) > 0): # initial
    stock = int(money // (int(a[0])))
    money = int(money % (int(a[0])))
    upflag = 1
    dnflag = 0

for i in range(n-2): # i=0,1,,,,n-3 (for n=7, n-3=4)
    if(int(a[i+1]) == int(a[i])):
        if((int(a[i+2]) - int(a[i+1]) < 0) and upflag == 1): # i+1 is local max so that to sell stock
            money = money + stock * (int(a[i+1]))
            stock = 0
            upflag = 1
            dnflag = 0
        elif((int(a[i+2]) - int(a[i+1]) > 0) and dnflag == 1): # i+1 is local min so that to sell stock
            stock = int(money // (int(a[i+1])))
            money = int(money % (int(a[i+1])))
            upflag = 0
            dnflag = 1

    elif(int(a[i+1]) - int(a[i]) > 0):
        upflag = 1
        if(int(a[i+2]) - int(a[i+1]) < 0): # i+1 is local max so that to sell stock
            money = money + stock * (int(a[i+1]))
            stock = 0
            upflag = 0

    elif(int(a[i+1]) - int(a[i]) < 0):
        dnflag = 1
        if(int(a[i+2]) - int(a[i+1]) > 0): # i+1 is local min so that to buy stock
            stock = int(money // (int(a[i+1])))
            money = int(money % (int(a[i+1])))
            dnflag = 0

if(int(a[n-1]) - int(a[n-2]) > 0): # sell @ final
    money = money + stock * (int(a[n-1]))
elif(int(a[n-1]) - int(a[n-2]) == 0):
    if(upflag == 1):
        money = money + stock * (int(a[n-1]))

print(money)
