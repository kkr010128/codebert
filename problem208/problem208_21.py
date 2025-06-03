import sys
n,m = map(int,input().split())

a = [0]*n
flag = [0]*n

for i in range(m):
    s,c = map(int,input().split())
    if s == 1 and c == 0 and n != 1:
        print(-1)
        sys.exit()

    if flag[s-1] == 0:
        flag[s-1] = 1
    else:
        #flag[s-1] == 1
        if a[s-1] != c:
            print(-1)
            sys.exit()
    a[s-1] = c



if a[0] == 0 and n != 1:
    a[0] = 1

print("".join(map(str,a)))
