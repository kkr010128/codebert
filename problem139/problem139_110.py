H,M,h,m,k = map(int, input().split())
time = h*60 + m - (H*60 + M) - k
print(time)