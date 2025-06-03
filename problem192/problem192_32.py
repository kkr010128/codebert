N = int(input())
A = list(map(int,input().split()))

cnt = {}
for i in A:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
total = 0
for i in cnt:
    if cnt[i]>=2:
        total += cnt[i] * (cnt[i]-1) // 2
        
for i in A:
    if cnt[i] == 1:
        print(total)
    else:
        #print(total - cnt[i]* (cnt[i]-1) // 2 + (cnt[i]-1) * (cnt[i]-2) // 2)
        print(total - (cnt[i]-1))