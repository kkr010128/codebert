n=int(input())
a=(n*(n+1))//2
z=n%3
x=n-z
x=x//3
s1=((x*(x+1))//2)*3
z=n%5
x=n-z
x=x//5
s2=((x*(x+1))//2)*5
z=n%15
x=n-z
x=x//15
s3=((x*(x+1))//2)*15
print (a-s1-s2+s3)