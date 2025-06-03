from collections import deque
n , k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9 + 7
ans = 1
plus = []
minus = []

if n == k:
    for i in range(n):
        ans *= a[i]
        ans %= mod
    print(ans)
    exit()
    
for i in range(n):
    if a[i] >= 0:
        plus.append(a[i])
    elif a[i] < 0:
        minus.append(a[i])

if not plus and k % 2 == 1:
    minus.sort(reverse=True)
    for i in range(k):
        ans *= minus[i]
        ans %= mod
    print(ans)
    exit()

plus.sort(reverse=True)
minus.sort()
plus = deque(plus)
minus = deque(minus)

cou = []
while True:
    if len(cou) == k:
        break
    elif len(cou) == k-1:
        cou.append(plus.popleft())
        break
    else:
        if len(plus)>=2 and len(minus)>=2:
            p1 = plus.popleft()
            p2 = plus.popleft()
            m1 = minus.popleft()
            m2 = minus.popleft()
            if p1*p2 > m1*m2:
                cou.append(p1)
                plus.appendleft(p2)
                minus.appendleft(m2)
                minus.appendleft(m1)
            else:
                cou.append(m1)
                cou.append(m2)
                plus.appendleft(p2)
                plus.appendleft(p1)
        elif len(plus) < 2:
            m1 = minus.popleft()
            m2 = minus.popleft()
            cou.append(m1)
            cou.append(m2)
        elif len(minus) < 2:
            p1 = plus.popleft()
            cou.append(p1)

        
for i in cou:
    ans *= i
    ans %= mod
print(ans)
