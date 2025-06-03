N = int(input())
d = list(map(int,input().split()))
sum = 0
for i in range(0,len(d)):
    for j in range(0,len(d)):
        if(i != j):
            sum += d[i] * d[j]
print(int(sum/2))