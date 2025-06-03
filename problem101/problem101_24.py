a,b,c=map(int,input().split())
k=int(input())
f=0
for i in range(1,k+1):
    d=c*(2**i)
    e=b*(2**(k-i))
    if a<e<d:
        f=1
print('Yes' if f else 'No')