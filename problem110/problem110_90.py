from itertools import combinations

h,w,k = map(int,input().split())
mat = [input() for i in range(h)]
r = [0 for i in range(h)]
c = [0 for i in range(w)]
black = 0
for i in range(h):
    for j in range(w):
        if mat[i][j]=="#":
            r[i] += 1
            c[j] += 1
            black += 1

ans = 0
for i in range(h):
    for combr in combinations(range(h),i):
        for j in range(w):
            for combc in combinations(range(w),j):
                temp = 0
                for x in combr:
                    temp += r[x]
                for y in combc:
                    temp += c[y]
                overlap = 0
                for x in combr:
                    for y in combc:
                        if mat[x][y]=="#":
                            overlap += 1
                if black+overlap-temp==k:
                    ans += 1

print(ans)
