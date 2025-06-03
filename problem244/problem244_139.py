il = [int(k) for k in input().split()]
K = il[0]
X = il[1]

if 500 * K >= X:
    print("Yes")
else:
    print("No")
