
from bisect import bisect_left

N = int(input())
S = input()

d = {"R": [], "G": [], "B": []}
for i in range(N):
    d[S[i]].append(i)


def find(x, y, z):
    total = len(z)
    res = 0
    for i in x:
        for j in y:
            if i > j:
                continue

            # Find k > j
            k = bisect_left(z, j)

            # Find k == 2 * j - i
            k0 = bisect_left(z, 2 * j - i)
            flag = int(k0 >= k and k0 < total and z[k0] == 2 * j - i)
            res += total - k - flag

    return res


ans = 0
ans += find(d["R"], d["G"], d["B"])
ans += find(d["R"], d["B"], d["G"])
ans += find(d["G"], d["R"], d["B"])
ans += find(d["G"], d["B"], d["R"])
ans += find(d["B"], d["R"], d["G"])
ans += find(d["B"], d["G"], d["R"])
print(ans)
