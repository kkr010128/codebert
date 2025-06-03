N = int(input())


hash = {}
end = int(N ** (1/2))
for i in range(2, end + 1):
    while N % i == 0:
        hash[i] = hash.get(i, 0) + 1
        N = N // i
if N != 1:
        hash[i] = hash.get(i, 0) + 1



count = 0
trans = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

res = 0
for i in hash.values():
    for j in range(len(trans)):
        if i > trans[j]:
            continue
        elif i == trans[j]:
            res += (j + 1)
            break
        else:
            res += j
            break



print(res)