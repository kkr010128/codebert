N = int(input())
N_List = {i:0 for i in range(1,N+1)}
E_List = list(map(int,input().split()))
for i in E_List:
    N_List[i] += 1

for i in N_List.values():
    print(i)