import math

n = input()

for i in range(n):
    flag = 0
    a = map(int, raw_input().split())
    if(pow(a[0],2)+pow(a[1],2) == pow(a[2],2)):
        flag = 1
    if(pow(a[1],2)+pow(a[2],2) == pow(a[0],2)):
        flag = 1
    if(pow(a[2],2)+pow(a[0],2) == pow(a[1],2)):
        flag = 1
    if flag == 1:
        print "YES"
    else:
        print "NO"