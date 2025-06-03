n = int(input())
l = list(map(int,input().split()))
l.sort(reverse = True)

ans = 0

for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i] != l[j] != l[k] and l[i] < l[j] + l[k]:
                ans +=1

print(ans)