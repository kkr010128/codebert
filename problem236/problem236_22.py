H = int(input())
W = int(input())
N = int(input())

p = -1
if H > W:
    p = H
else:
    p = W

count = 1
result = 1
while True:
    result = count * p
    if result >= N:
        print(count)
        break
    else:
        count += 1
