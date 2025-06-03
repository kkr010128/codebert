import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
ans = ""
for c in s:
    ans += chr((ord(c)+n-ord("A"))%26 + ord("A"))
print(ans)