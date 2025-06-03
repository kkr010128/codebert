#abc145_d
m = 10**9+7
x,y = map(int,input().split())
fac =[0]*(10**6+1)
a = max(x,y)
b = min(x,y)
cnt = 0
fac[0]=1

while a != b:
    a -= 2
    b -= 1
    cnt +=1
    fac[cnt] = (fac[cnt-1]*cnt)%m

    if a<0 or b <0:
        print(0)
        exit()
c = a//3
d = cnt
if a%3 != 0:
    print(0)
    exit()
    
else:
    while a != 0:
        a -= 1
        b -= 2
        cnt +=1
        fac[cnt] = (fac[cnt-1]*cnt)%m

        a -= 2
        b -= 1
        cnt +=1
        fac[cnt] = (fac[cnt-1]*cnt)%m

n = ((fac[cnt])%m)*(pow(fac[c+d],m-2,m))*(pow(fac[c],m-2,m))
print(n%m)
