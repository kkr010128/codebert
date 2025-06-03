n=int(input())
s=100000
for i in range(n):
    s=s*1.05
    if s%1000==0:
        s=s
    else:
        s=(s//1000)*1000+1000
print(int(s))
