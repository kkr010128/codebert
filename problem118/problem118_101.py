n = int(input())
sum=0
for j in range(1,n+1):
    sum+=(n//j)*(n//j+1)//2*j
print(sum)