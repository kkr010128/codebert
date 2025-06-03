(a,b,m),x,y,*c=[list(map(int, i.split())) for i in open(0)]
print(min([x[~-i]+y[~-j]-k for i,j,k in c]+[min(x)+min(y)]))