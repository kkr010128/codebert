n,k=map(int,input().split())
p_list=list(map(int,input().split()))
p_list=sorted(p_list)
new_p_list=[]
for i in range(k):
    new_p_list.append(p_list[i])
print(sum(new_p_list))