import re,sys
al=[chr(ord('a')+i) for i in range(26)]
s=sys.stdin.read().lower()
for i in range(26):
    cnt=len(re.findall(al[i],s))
    print("{} : {}".format(al[i],cnt))
