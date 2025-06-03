N=int(input())
result=0
for i in range(0,N+1):
    if i%2 != 0:
        result+=1
    else: 
        result+=0
print(float(result/N))