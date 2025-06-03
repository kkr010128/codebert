n, k = map(int,input().split())
w = [0]*n

for i in range(n):
    w[i] = int(input())

minP = max(max(w), sum(w)//k)
maxP = sum(w)
    
left = minP
right = maxP

while left < right:
    mid = (left + right) // 2
    load = 0
    cnt_track = 1
    flag = 1
    for i in range(n):
        load += w[i]
        if load > mid:
            load = w[i]
            cnt_track += 1

        if cnt_track > k:
                flag = 0
                break
    if flag:
        right = mid
    else:
        left = mid + 1
            
print(left)
