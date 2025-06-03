iterator = [["NS", "S"], ["NT", "T"]]
var = {}
for i, j in iterator:
    var[i] = int(input())
    var[j] = [int(k) for k in input().split()]
res = 0
for T in var["T"]:
    if T in var["S"]:
        res += 1
print(res)