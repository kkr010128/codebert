M=998244353
n,m,k=map(int,input().split())
a,c=0,1
for i in range(k+1):
  a+=c*m*pow(m-1,n+~i,M)
  c=c*(n+~i)*pow(i+1,-1,M)%M
print(a%M)