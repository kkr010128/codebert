N_dict  = {i:0 for i in list(map(str,input().split()))}
N_List = list(map(int,input().split()))
ct = 0
for i in N_dict.keys():
    N_dict[i] = N_List[ct]
    ct += 1

N_dict[str(input())] -= 1
print(" ".join(list(map(str,N_dict.values()))))
