import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
if s[-1]=="s":
    s += "es"
else:
    s += "s"
print(s)