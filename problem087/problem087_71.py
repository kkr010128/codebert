n=int(input())
sums=0
for i in str(n):
    sums+=int(i)
print('Yes' if sums%9==0 else 'No')