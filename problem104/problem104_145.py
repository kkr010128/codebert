L, R, d  = map(int, input().split())
pq = 0
for x in range(R+1):
    y = d * x
    if y>=L and y<=R:
        pq += 1
print(pq)