def main(n,k,a):
  for _ in range(k):
    b=[0]*(n+1)
    for i,j in enumerate(a):
      b[max(0,i-j)]+=1
      b[min(n,i+j+1)]-=1
    for i in range(n):
      b[i+1]+=b[i]
    if a==b:break
    a=b
  print(*a[:-1])
N,K,*A=map(int,open(0).read().split())
main(N,K,A)