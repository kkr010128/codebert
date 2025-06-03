t=input()
h = t/3600
m = t%3600/60
s = t%60
print':'.join(map(str,[h,m,s]))