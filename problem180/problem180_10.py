n,k = map(int,input().split())
amari = n%k
tmp = abs(amari-k)
print(min(amari,tmp))