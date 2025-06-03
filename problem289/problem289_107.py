import numpy as np
a, b, x = map(int, input().split())
ans = 0
if (a*a*b/2) <= x:
    ans = np.rad2deg(np.arctan((2*(a*a*b-x))/(a*a*a)))
else:
    ans = np.rad2deg(np.arctan((a*b*b)/(2*x)))
print('{:.10f}'.format(ans))
