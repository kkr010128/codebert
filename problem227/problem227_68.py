from collections import deque
N,K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)
deqH = deque(H)
if N <= K:
    print(0)
else:
    for i in range(K):
        deqH.popleft()
        #H.remove(max(H))
        #print(H)
    print(sum(deqH))
