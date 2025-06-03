n = int(input())

r = n % 27
if r == 13 or r == 26:
    print(':(')
elif r ==0:
    x = int(100*n/108)
    print(x)
else:
    for i in range(1, 25):
        if 1.08*(i-1) < r <= 1.08*i:
            break
    x = int(100*(n - i)/108) + i
    print(x)