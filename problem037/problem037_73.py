n = int(input())

h = int(n / 3600)
m = int((n-h*3600) / 60)
s = n - h * 3600 - m * 60

print(':'.join(map(str, [h,m,s])))