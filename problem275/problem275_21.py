x, y = map(int,input().split())
print((max(4-x, 0) + max(4-y, 0) + 4*max(3-x-y, 0)) * 100000)