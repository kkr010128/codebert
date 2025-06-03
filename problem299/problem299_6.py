import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
aa = [(num,i) for i,num in enumerate(a)]
aa.sort()
write(" ".join(map(str, [item[1]+1 for item in aa])))