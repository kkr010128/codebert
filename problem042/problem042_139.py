# Python 3+
#-------------------------------------------------------------------------------
import sys

#ff = open("test.txt", "r")
ff = sys.stdin

cnt = 1
for line in ff :
    if int(line) == 0 : break
    print("Case {0}: {1}".format(cnt, line), end="")
    cnt += 1