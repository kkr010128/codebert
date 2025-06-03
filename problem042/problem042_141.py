import sys

s = sys.stdin

cnt = 1
for i in s:
    if int(i)== 0:
        break
    print("Case {0}: {1}".format(cnt,i),end="")
    cnt += 1