a,b = map(int,input().split())
num = 0
if a <= b:
    for i in range(b):
        num += a * 10**i
    print(num)
else:
    for i in range(a):
        num += b * 10**i
    print(num)