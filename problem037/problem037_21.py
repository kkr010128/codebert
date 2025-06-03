value = int(input())

h, value = value // 3600, value - (value//3600) * 3600
m, value = value //60, value - (value // 60) * 60
s = value 

print("%d:%d:%d" %(h,m,s))
