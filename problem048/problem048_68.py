n=input()
a=map(int,raw_input().split())
max=-10000000000
min=10000000000
sum=0
for i in range(n):
    sum=sum+a[i]
    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
print('%d %d %d'%(min,max,sum))