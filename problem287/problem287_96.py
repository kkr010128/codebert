import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
for i in range(1,10):
    if n%i==0 and n//i<10:
        ans = "Yes"
        break
else:
    ans = "No"
print(ans)