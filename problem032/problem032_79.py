n=eval(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
def minkowski(p,x_1,x_2,n):
    if p==0:
        return float(max([abs(x_1[i]-x_2[i]) for i in range(n)]))
    else:
        return sum([(abs(x_1[i]-x_2[i]))**p for i in range(n)])**(1/p)
for i in range(4):
    print(minkowski((i+1)%4,x,y,n))