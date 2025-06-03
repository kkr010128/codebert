import numpy as np

N = int(input())
A = list(map(int,input().split()))

a = np.array(A)

odd = a[a%2 == 0]

if np.sum((odd%3 != 0)&(odd%5 != 0)) == 0:
    print('APPROVED')
else:
    print('DENIED')
