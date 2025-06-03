n=int(input())
s=100000
for i in range(n):
    s*=1.05
    p=s%1000
    if p!=0:
        s+=1000-p
print(int(s))
