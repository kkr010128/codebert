val = input().split(' ')
N = int(val[0])
A = int(val[1])
B = int(val[2].strip())

if (B - A) % 2 == 0:
    print((B-A)//2)
else:
    diff = N - B if A - 1 > N - B else A - 1
    flip = diff + 1
    distance = (B - A - 1) // 2
    print(flip + distance)
