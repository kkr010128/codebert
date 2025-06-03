k = int(input())
a,b = map(int,input().split())
n = range(k,1001,k)
if any(a <= i and i <= b for i in n):
    print('OK')
else:
    print('NG')
