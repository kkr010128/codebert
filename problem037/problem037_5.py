time = int(input())

h = time // 3600
m = (time // 60) % 60
t = time % 60
print("{0}:{1}:{2}" .format(h, m, t))