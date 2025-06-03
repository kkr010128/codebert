h1,m1,h2,m2,k=map(int,input().split())
if h1>h2:
    h2+=24
p=(h2-h1)*60+(m2-m1)
print(p-k)