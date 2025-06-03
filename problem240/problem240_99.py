n, m = map(int, input().split())
listAC = [0] * n
listWAAC = [0] * n
listWA = [0] * n
for i in range(m):
    p, s = map(str, input().split())
    p = int(p) - 1
    if listAC[p] == 1:
        continue
    if s == 'AC':
        listAC[p] += 1
        listWAAC[p] += listWA[p]
        continue
    listWA[p] += 1

print(sum(listAC), sum(listWAAC))
