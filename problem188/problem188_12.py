import heapq

X,Y,A,B,C = map(int, input().split())
p_list = sorted([(-v, 'p') for v in map(int, input().split())])
q_list = sorted([(-v, 'q') for v in map(int, input().split())])
r_list = sorted([(-v, 'r') for v in map(int, input().split())])

res = 0
r_cnt = 0
for v, k in heapq.merge(p_list, q_list, r_list):
    v = -v
    if X+Y-r_cnt == 0:
        break
    if k == 'p':
        if X != 0:
            X -= 1
            res += v
        continue
    
    if k == 'q':
        if Y != 0:
            Y -= 1
            res += v
        continue

    res += v
    r_cnt += 1

print(res)
