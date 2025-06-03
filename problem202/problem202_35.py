import numpy as np

N,A,B = (int(x) for x in input().split())

C = A+B
set = N // C

ans = A if (N-C*set) >= A else N-C*set

ans += set*A

print(ans)
