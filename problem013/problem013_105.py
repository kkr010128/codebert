num= n = int(input())

price = []
max_pro = -999999999

while(n>0):
    x = int(input())
    price.append(x)
    n -= 1
min = price[0]
for i in range(1,num):
    pro = price[i]-min

    if(max_pro < pro):
        max_pro = pro
    if(min > price[i]):
        min = price[i]
print ("{0}".format(max_pro))