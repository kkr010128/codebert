n,x,t=map(int,input().split())
count = n // x
if n % x == 0:
    pass
else:
    count += 1
print(count * t)