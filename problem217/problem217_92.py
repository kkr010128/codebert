import numpy as np
stdin = open(0)

A = np.fromstring(stdin.read(), np.int64, sep=' ')[1:]
A = A[A % 2 == 0]
if np.all((A % 3 == 0) | (A % 5 == 0)):
    print('APPROVED')
else:
    print('DENIED')