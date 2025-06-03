#!/usr/bin/env python3
from collections import defaultdict

n,k = map(int,input().split())
a = list(map(int,input().split()))
cum_sum = [0]*(n+1)#累積和 - i （要素すう）modk
for i in range(n):
  cum_sum[i+1] = (cum_sum[i]+a[i]-1) % k#cum_sum[i]-iが一定
D = defaultdict(int)

count = 0
for i in range(n+1):
  count += D[cum_sum[i]] #key が場所、val がcum_sumの値
  D[cum_sum[i]] += 1
  if i-k+1 >= 0:#区間の長さがあまりよりも小さいなら
    D[cum_sum[i-k+1]] -=1
print(count)