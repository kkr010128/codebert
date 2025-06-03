#!/usr/bin/env python3

H1, M1, H2, M2, K = map(int, input().split())

ans = 0
if M1 <= M2:
    ans = (H2-H1) * 60 + M2 - M1 - K
else:
    ans = (H2-H1-1) * 60 + (60-M1) + M2 - K

if ans < 0:
    print(0)
else:
    print(ans)
