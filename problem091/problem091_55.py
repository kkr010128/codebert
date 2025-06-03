n = int(input())
l = list(map(int,input().split()))

cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                nagasa = sorted([l[i],l[j],l[k]])
                if nagasa[0] + nagasa[1] > nagasa[2]:
                    cnt += 1
print(cnt // 6)