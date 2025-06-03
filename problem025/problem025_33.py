
n = (int)(input())
a = list(map(int, input().split(" ")))
q = (int)(input())
m = list(map(int, input().split(" ")))
lst = []
for i in range(2 ** n, 0, -1):
    temp = 0
    for j in range(n):
        if (i >> j) & 1:
            temp += a[j]
    lst.append(temp)
for k in range(q):
    if m[k] in lst:
        print("yes")
    else:
        print("no")
