s = list(map(int,input().split()))

h = 60 * (s[2]-s[0])
m = s[3] - s[1]
k = s[4]
print(h+m-k)