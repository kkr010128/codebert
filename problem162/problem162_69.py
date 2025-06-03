n,m = map(int,input().split())
a = 0
for i in range(m):
    if n % 2 == 0 and n % 4 != 0 and n-4*i-2 == 0:
        a = 1
    elif n % 4 == 0 and i == (n//2-1) // 2 + 1:
        a = 1
    print('{} {}'.format(i+1, n-i-a))