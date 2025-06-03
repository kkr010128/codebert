import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

a = ri()
li = sorted(rl(), reverse=True)
cnt = 0
for i in range(a-2):
    for j in range(i+1, a-1):
        left = j+1
        right = a
        lii = li[i]
        lij = li[j]
        if lii >= lij + li[j+1]:
            continue
        while right-left > 1:
            t = (left + right)//2
            lit = li[t]
            if lii < lij + lit:
                left = t
            else:
                right = t
        cnt += left-j
print(cnt)

















