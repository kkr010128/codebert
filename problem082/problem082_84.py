"""B."""

import sys

input = sys.stdin.readline  # noqa: A001

S = input()[:-1]
T = input()[:-1]

S_L = len(S)
T_L = len(T)
ans = T_L

for i in range(S_L - T_L + 1):
    S_2 = S[i:i + T_L]
    match = 0
    for v1, v2 in zip(S_2, T):
        match += bool(v1 != v2)
    ans = min(ans, match)

print(ans)

exit(0)