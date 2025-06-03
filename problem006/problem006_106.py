n=int(input())
x=100000
for i in range(n):
    x*=1.05
    if x%1000>0:
        x=x-(x%1000)+1000
    else:
        pass
print(int(x))
