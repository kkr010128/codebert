n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
a=[]
b=[]
for i in range(n):
  a.append(l[i][0]+l[i][1])
  b.append(l[i][0]-l[i][1])
print(max(max(a)-min(a),max(b)-min(b)))