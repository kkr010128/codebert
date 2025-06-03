
time = input()
h = time / 3600
m = time % 3600 / 60
s = time % 3600 % 60
print ":".join(map(str,[h,m,s]))