h, a = map(int, input().split(' '))
for i in range(10001):
    if h <= a*i:
        print(i)
        exit(0)