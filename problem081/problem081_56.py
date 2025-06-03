#template
def inputlist(): return [int(j) for j in input().split()]
#template
"""
H,W = inputlist()
st = inputlist()
gl = inputlist()
maze = ['0']*H
for i in range(H):
    maze[i] = list(input())
table = [[10**9+7]*W for _ in range(H)]

"""
D,T,S = inputlist()
time = D//S + int(D%S != 0)
if time <= T:
    print("Yes")
else:
    print("No")
