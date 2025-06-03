import heapq

X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
p = p[:X]
q = q[:Y]
all_apples = p + q + r
all_apples.sort(reverse=True)
print(sum(all_apples[:X+Y]))