import numpy as np

a, b, x = map(int,input().split())
th = a**2 * b / 2
if x <= th:
    ans = np.arctan(a*b**2/2/x)
else:
    ans = np.arctan((2*b-2*x/a**2)/a)
print(np.degrees(ans))