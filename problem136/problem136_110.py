N = int(input())


hash = {}
end = int(N ** (1/2))
for i in range(2, end + 1):
    while N % i == 0:
        hash[i] = hash.get(i, 0) + 1
        N = N // i
if N != 1:
        hash[i] = hash.get(i, 0) + 1


count = 1
res = 0
for i in hash.values():
    count = 1
    while i >= count:
        res += 1
        i -= count
        count += 1

print(res)