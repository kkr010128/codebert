def get_depth(graph,tmp_depth,vertex_list,depth_list):
    new_vertex_list=[]
    for vertex in vertex_list:
        for j in range(len(depth_list)):
            if(graph[vertex][j]!=0 and depth_list[j]==-1):
                depth_list[j]=tmp_depth + 1
                new_vertex_list.append(j)
    if(len(new_vertex_list)!=0):
        get_depth(graph,tmp_depth+1,new_vertex_list,depth_list)


#グラフの作成
n=int(input())
graph=[[0]*n for loop in range(n)]
for loop in range(n):
    tmp_ope=list(map(int,input().split()))
    for j in range(tmp_ope[1]):
        graph[tmp_ope[0]-1][tmp_ope[j+2]-1]=1


depth_list=[-1]*n
depth_list[0]=0
vertex_list=[0]
get_depth(graph,0,vertex_list,depth_list)

for i in range(n):
    print(f"{i+1} {depth_list[i]}")
