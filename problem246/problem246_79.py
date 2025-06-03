#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]
import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

if (p == q):
    print(0)
    exit()

seq = []
for i in range(1,n+1):
    seq.append(i)

t = list(itertools.permutations(seq))

ans = []
for i in range(len(t)):
    if list(t[i]) == p or list(t[i]) == q:
        ans.append(i)

print(ans[1]-ans[0])
