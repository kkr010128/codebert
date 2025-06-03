N=int(input())

p=0
for i in range(N+1):
    if i%2==1:
        p +=1
print(p/N)