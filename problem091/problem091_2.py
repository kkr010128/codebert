N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i] != L[j] and L[j] != L[k] and L[i] != L[k] and max(L[i],L[j],L[k]) < sum([L[i],L[j],L[k]])/2:
                count+=1
print(count)