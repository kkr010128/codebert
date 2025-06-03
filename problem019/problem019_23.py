n, q = map(int, input().split())
que = []
for i in range(n):
    p, t = map(str, input().split())
    que.append([p, int(t)])
total = 0
while que != []:
    pt = que.pop(0)
    if pt[1] <= q:
        total += pt[1]
        print(pt[0], total)
    else:
        total += q
        que.append([pt[0], pt[1]-q])
