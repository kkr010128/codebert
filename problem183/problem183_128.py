n=int(input())
a=n>2
for i in range(2,int(n**.5)+1):
 m=n
 while m%i<1:m//=i
 a+=(m%i<2)+(~-n%i<(i<~-n//i))
print(a+1)