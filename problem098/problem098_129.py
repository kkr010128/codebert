n = int(input())
c = list(input())
 
nR = c.count("R")
 
if nR == 0 or nR == len(c):
    print(0)
else:
    print(c[:nR].count("W"))