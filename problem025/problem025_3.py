def solve(a, m, sumA):
    if m < 0 or m > sumA:
        return False
    if m == 0:
        return True
    if len(a) == 0:
        return False
    return solve(a[1:], m - a[0], sumA) or solve(a[1:], m, sumA)

n = int(input())
tmp = input().split()
a = []
for i in range(n):
    a.append(int(tmp[i]))
q = int(input())
tmp = input().split()
m = []
for i in range(q):
    m.append(int(tmp[i]))

sumA = sum(a)

for i in range(q):
    if solve(a, m[i], sumA):
        print("yes")
    else:
        print("no")

