t = list(map(int, input().split()))
m = (t[2] - t[0]) * 60 + (t[3] - t[1])
print(m - t[4])