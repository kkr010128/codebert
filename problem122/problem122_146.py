n = int(input())
arr = [int(x) for x in input().split()]
q = int(input())

dictA = {}
for i in arr:
    if dictA.get(i): dictA[i] += 1
    else: dictA[i] = 1

summ = sum(arr)

for i in range(q):
    b, c = list(map(int, input().split()))
    if dictA.get(b):
        summ = summ - (dictA[b]*b) + (dictA[b]*c)
        if dictA.get(c): dictA[c] += dictA[b]
        else: dictA[c] = dictA[b]
        del dictA[b]
    print(summ)
