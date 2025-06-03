result = []
while True:
    m, f, r = map(int, input().split())
    if (m, f, r) == (-1, -1, -1):
        break
    if m == -1 or f == -1:
        result.append('F')
        continue
    if m + f >= 80:
        result.append('A')
    if 80 > m + f >= 65:
        result.append('B')
    if 65 > m + f >= 50:
        result.append('C')
    if 50 > m + f >= 30:
        result.append(['D', 'C'][r >= 50])
    if 30 > m + f:
        result.append('F')
for r in result:
    print(r)