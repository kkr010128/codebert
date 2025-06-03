def line(): return [int(i) for i in input().split(" ")]
n = line()[0]
for i in line(): n -= i
print(max(-1, n))