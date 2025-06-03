import itertools
N = int(input())
N_List = [list(map(int,input().split())) for _ in range(N)]
ans = 0
cnt = 0
for Sort_List in itertools.permutations(N_List, N):
    cnt += 1
    cans = 0
    for v in range(1,N):
        cans += ((Sort_List[v][0] - Sort_List[v-1][0])**2 + (Sort_List[v][1] - Sort_List[v-1][1])**2)**0.5
    ans += cans

print(ans/cnt)