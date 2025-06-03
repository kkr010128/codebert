import sys
n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
for i in range(n-2):
    if ls[i][0] == ls[i][1]:
        if ls[i+1][0] == ls[i+1][1]:
            if ls[i+2][0] == ls[i+2][1]:
                print("Yes")
                sys.exit()
print("No")