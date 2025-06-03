n=int(input())
s=100000
for i in range(n):
    s*=1.05
    m = s % 1000
    if m!=0:
        s=s-m+1000
print(int(s))
