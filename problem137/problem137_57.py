import statistics

n = int(input())
a = []
b = []
for i in range(n):
    ai,bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

ma = statistics.median(a)
mb = statistics.median(b)

if n % 2 == 1:
    ans = mb - ma + 1
else:
    ma = int(ma * 2)
    mb = int(mb * 2)
    ans = mb - ma + 1

print(ans)
