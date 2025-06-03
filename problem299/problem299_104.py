N = int(input())
A = list(map(int, input().split()))
import numpy as np
A = np.array(A)
ans = np.argsort(A)
ans = list(str(a + 1) for a in ans)
ans = ' '.join(ans)
print(ans)