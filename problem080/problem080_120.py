def seekDistance(n,nodes):
    max_z,min_z = searchMaxAndMinZ(n,nodes)
    max_w,min_w = searchMaxAndMinW(n,nodes)
    return max(max_z-min_z,max_w-min_w)

def searchMaxAndMinZ(n,nodes):
    max_z = -1
    min_z = 2 * 10 ** 9
    for i in range(n):
        curr_z = nodes[i][0] + nodes[i][1]
        if(curr_z > max_z):
            max_z = curr_z
        if(curr_z < min_z):
            min_z = curr_z
    return max_z,min_z

def searchMaxAndMinW(n,nodes):
    max_w = -10**9
    min_w = 2 * 10 ** 9
    for i in range(n):
        curr_w = nodes[i][0] - nodes[i][1]
        if (curr_w > max_w):
            max_w = curr_w
        if (curr_w < min_w):
            min_w = curr_w
    return max_w, min_w

n = int(input())
nodes = [list(map(int,input().split())) for i in range(n)]
print(seekDistance(n,nodes))