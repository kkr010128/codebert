import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a= [0]*n
b= [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

if n%2 ==1:
    a.sort()
    b.sort()
    xmin= a[int((n-1)/2)]
    xmax= b[int((n - 1) / 2)]

    print(int(xmax-xmin+1))

if n%2 ==0:
    a.sort()
    b.sort()
    xmin = a[int(n/2-1)]+a[int(n/2)]
    xmax = b[int(n / 2 - 1)] + b[int(n / 2)]
    print(int((xmax-xmin)+1))