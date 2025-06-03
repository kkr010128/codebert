from collections import deque
def deque_divisor(n):
    d = deque()
    for i in range(int(n**(1/2)),0,-1):
        if i**2 == n:
            d.append(i)
            continue
        if n % i == 0:
            d.appendleft(i)
            d.append(n//i)
    return d

n = int(input())

candidate = (set(deque_divisor(n)) | set(deque_divisor(n-1)))
candidate.discard(1)

ans = 0

for i in candidate:
    k = n
    while k % i == 0:
        k //= i
    k %= i
    if k == 1:
        ans += 1

print(ans)