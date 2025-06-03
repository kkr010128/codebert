n, k = map(int, input().split(' '))
w = [int(input()) for i in range(n)]

max_w = 100000 * 10000
P = 0
left = 0
right = max_w

def check(p):
    sum = 0
    count = 1
    for i in range(n):
        if(sum + w[i] > p):
            count += 1
            sum = w[i]
            if(count > k or w[i] > p):
                return False
        else:
            sum += w[i]

    return True

while(right - left > 1):
    mid = (left + right) // 2
    if(check(mid)):
        right = mid
        P = mid
    else:
        left = mid

print(P)
