n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(n) :
    if i == 0 :
        mn = p[i]
        count += 1
    else :
        if mn > p[i] :
            mn = p[i]
            count += 1
print(count)
