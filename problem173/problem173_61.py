n=int(input())

a=n//3
b=n//5
c=n//15

suma=(0+a*3)*(a+1)//2
sumb=(0+b*5)*(b+1)//2
sumc=(0+c*15)*(c+1)//2

print((n+1)*n//2-suma-sumb+sumc)