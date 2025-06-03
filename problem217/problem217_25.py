n = int(input())
a = list(map(int,input().split()))
if all(a[i]%2 or a[i]%3 == 0 or a[i]%5 == 0 for i in range(n)):
    print('APPROVED')
else:
    print('DENIED')
