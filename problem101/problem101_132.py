a, b, c = map(int, input().split())
k = int(input())
count = 0
while True:
    if b > a:
        break
    b *= 2
    count += 1
while True:
    if c > b:
        break
    c *= 2
    count += 1

if count <= k:
    print('Yes')
else:
    print('No')
