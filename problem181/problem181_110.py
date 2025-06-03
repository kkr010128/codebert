import queue

K = int(input())

Q = queue.Queue()

for i in range(1, 10):
    Q.put(i)

ans = 1
for k in range(K):
    ans = Q.get()
    ansm = ans % 10
    if ans%10 != 0:
        Q.put(10 * ans + ansm - 1)
    Q.put(10 * ans + ansm)
    if ans%10 != 9:
        Q.put(10 * ans + ansm + 1)

print(ans)