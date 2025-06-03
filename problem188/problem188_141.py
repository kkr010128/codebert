# N = int(input())
import heapq

X, Y, A, B, C = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

p = sorted(p, reverse=True)[:X]
q = sorted(q, reverse=True)[:Y]
heapq.heapify(p)
heapq.heapify(q)
r_asc = sorted(r, reverse=True)

for r in r_asc:
    p_min = heapq.heappop(p)
    q_min = heapq.heappop(q)
    if p_min > q_min and r > q_min:
        heapq.heappush(q, r)
        heapq.heappush(p, p_min)
    elif q_min >= p_min and r > p_min:
        heapq.heappush(p, r)
        heapq.heappush(q, q_min)
    else:
        heapq.heappush(q, q_min)
        heapq.heappush(p, p_min)
        break
print(sum(p) + sum(q))

