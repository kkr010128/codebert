N=int(input())
k=0
for i in range(N+1):
    if i%3==0 or i%5==0:
        k+=0
    else:
        k+=i
print(k)