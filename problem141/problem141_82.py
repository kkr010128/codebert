N = int(input())
A = list(map(int,input().split()))

SUM = sum(A)

ans = 0
node = 1
for i,leaf in enumerate(A):
    if i == 0:
        non_leaf = 1 - leaf
        ans += 1
        if non_leaf <0:
            print(-1)
            exit()
    else:
        left,right = non_leaf,non_leaf*2
        if SUM < left or non_leaf <= 0:
            print(-1)
            exit()
        node = min(right,SUM)
        ans += node
        non_leaf = node - leaf
        SUM -= leaf
        if non_leaf < 0:
            print(-1)
            exit()

print(ans)