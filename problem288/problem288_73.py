n=int(input())
rootn=int(n**(0.5))+1
m=10**20
for i in range(1,rootn):
    if n/i==n//i:
        m=min(m,i+n//i)
print(m-2)