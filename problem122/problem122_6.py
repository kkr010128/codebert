n = int(input())
a = list(map(int, input().split()))
q = int(input())
s = sum(a)

count = [0] * 100000
for i in range(n):
    count[a[i] - 1] += 1
    
for i in range(q):
    o = list(map(int, input().split()))
    s += (o[1] - o[0]) * count[o[0] - 1]
    count[o[1] - 1] += count[o[0] - 1]
    count[o[0] - 1] = 0
    print(s)