N = int(input())
L = [int(i) for i in input().split()]

count = 0
L.sort()
for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            if L[i]!=L[j]!=L[k]:
                if ((L[i]+L[j]>L[k]) and (L[j]+L[k]>L[i]) and (L[i]+L[k]>L[j])) :
                    count += 1
                
print(count)