n=int(input())
s=100000
for _ in range(n):
    s*=1.05
    if s%1000!=0:
        s+=1000-s%1000
print(int(s))