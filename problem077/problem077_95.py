# B 
a, b, c, d = list(map(int, input().split(" ")))
numlist = [a*c, a*d, b*c, b*d]
maxnum = max(numlist)
print(maxnum)