n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

min = r[0]
max = -10 ** 12

for j in r[1:]:
    if j - min > max:
        max = j - min
    if min > j:
        min = j

print(max)