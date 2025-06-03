n,m=map(int,input().split())
for i in range(m):
    print(i+1,2*m-i+(n%2==0 and 2*(m-i)-1>=n//2))