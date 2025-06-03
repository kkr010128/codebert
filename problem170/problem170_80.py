po=pow(10,9)+7
n,k=map(int,input().split())
cc=0
for i in range(k,n+2):
  cc+=(n*i-i*(i-1)+1)%po
print(cc%po)