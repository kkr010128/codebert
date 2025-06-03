h,m,hh,mm,k = map(int,input().split())
x = hh*60-h*60+mm-m
print(x-k)