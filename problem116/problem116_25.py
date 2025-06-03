
import sys
input = sys.stdin.readline



def inps():
    return str(input())


s = inps().rsplit()[0]
t = inps().rsplit()[0]
cnt = 0
for i in range(len(s)):
    if s[i]!=t[i]:
        cnt+=1
print(cnt)

