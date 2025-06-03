n,k = map(int,input().split())
w = []

for loop in range(n):
    w.append(int(input()))

left = max(w)
right = 100000 * 10000
mid = (left+right)//2
ans = right

def check(P):
    tmp_sum = 0
    cnt = 1
    for loop in range(n):
        if tmp_sum + w[loop] <= P:
            tmp_sum += w[loop]
        else:
            tmp_sum = w[loop]
            cnt += 1
            if cnt > k:
                return False
    return True

while left <= right:
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
    mid = (left+right)//2

print(ans)
