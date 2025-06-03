n=int(input())
x=0
for i in range(n):
    if i==0:
        continue
    elif n//i==n/i:
        x+=(n//i)-1
    else:
        x+=n//i
     
print(x)