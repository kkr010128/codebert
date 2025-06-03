n,ans = int(input()),0
if not n%2:
    for i in range(1,30):
        ans+=n//(5**i*2)
print(ans)