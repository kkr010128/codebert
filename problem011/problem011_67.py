a=map(int,raw_input().split())
a.sort()
while a[1]%a[0]!=0:
 a[0],a[1]=a[1]%a[0],a[0]
print(a[0])