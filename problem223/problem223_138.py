n,k = map(int,input().split())
p = list(map(int,input().split()))
sum = 0
for i in range(n):
    p[i] = (1+p[i])/2
    if i<k-1:
        sum += p[i]
    elif i==k-1:
        sum += p[i]
        largest = sum
    else:
        sum = sum + p[i] - p[i-k]
        largest = max(largest,sum)
        
print(largest)
