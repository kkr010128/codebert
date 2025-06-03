n=int(input())
syakkin=100000
for i in range(n):
    syakkin*=1.05
    if syakkin%1000!=0:
        syakkin=syakkin-syakkin%1000+1000
print(int(syakkin))
