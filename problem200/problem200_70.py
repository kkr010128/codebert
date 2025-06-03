#B - Nice Shopping 
A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
X = []
Y = []
C = []
for i in range(M):
    x,y,c = map(int,input().split())
    X.append(x)
    Y.append(y)
    C.append(c)

#割引券を使う場合
pay_sale = [a[i-1]+b[j-1]-k for i,j,k in zip(X,Y,C)]
pay_ticket = min(pay_sale) 
#使わない場合
pay = min(a) + min(b)
print(min(pay,pay_ticket))