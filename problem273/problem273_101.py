# E - Rem of Sum is Num
import queue
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A[i] - 1) % K

v_set = set(S)
mp = {v: 0 for v in v_set}
ans = 0
q = queue.Queue()
for i in range(N + 1):
    ans += mp[S[i]]
    mp[S[i]] += 1
    
    q.put(S[i])
    if q.qsize() == K:
        mp[q.get()] -= 1

print(ans)