n = int(raw_input())
  
d = [0 for i in range(n)]
f = [0 for i in range(n)]
a = [[0 for i in range(n)] for j in range(n)]
st = [0 for i in range(n)]
time = [0]
g = [0 for i in range(n)]
  
  
def dfs_visit(s):
    st[s] = 1
    time[0] += 1
    d[s] = time[0]
      
    for k in range(n):  
      if a[s][k] == 1 and st[k] == 0:
          dfs_visit(k)
    st[s] ==2
    time[0] += 1
    f[s] = time[0]
  
def main():
    for s in range(n):
        if st[s] == 0:
            dfs_visit(s)
    for s in range(n):
        print '%d %d %d' %(s+1, d[s], f[s])
  
for i in range(n):
    g = map(int, raw_input().split())
    for j in range(g[1]):
        a[g[0]-1][g[2+j]-1] = 1
  
main()