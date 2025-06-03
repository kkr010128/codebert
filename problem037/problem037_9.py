time = input()
h = time/3600
m = time/60%60
s = time%60
print "%d:%d:%d"% (h, m, s)