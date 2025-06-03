import itertools

N = int(input())

xy_ls = []
for i in range(N):
    A = int(input())
    xy = [list(map(int,input().split())) for j in range(A)]
    xy_ls.append(xy)

ans_ls = list(itertools.product([0,1], repeat=N))

max_ans = 0
for ans in ans_ls:
    flg = True
    for i in range(len(ans)):
        if ans[i]==1:
            for xy in xy_ls[i]:
                if ans[xy[0]-1] == xy[1]:
                    pass
                else:
                    flg = False
                    break
    if flg == True:
        max_ans = max(max_ans,sum(ans))

print(max_ans)