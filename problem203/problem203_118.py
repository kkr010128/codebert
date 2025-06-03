def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

a,b=sep()
for i in range(1,10005):
    if (i*8)//100==a and (i*10)//100==b:
        print(i)
        quit()
print(-1)