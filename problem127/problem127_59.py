import numpy as np
import numpy.linalg as linalg 

X, Y = map(int, input().split())

if Y%2 == 1:
  print('No')
else:
  A = np.array([[1, 1],
                [2, 4]])
  A_inv = linalg.inv(A)

  B = np.array([X , Y])

  C = np.dot(A_inv, B)
  if C[0] >= 0 and C[1] >= 0 :
    print('Yes')
  else:
    print('No')

