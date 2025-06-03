# ABC178D Manhattan
n = int(input())
z = []
w = []
for i in range(n):
    x,y = map(int, input().split())
    z.append(x-y)
    w.append(x+y)
    
z_ans = max(z)-min(z)
w_ans = max(w)-min(w)
print(max(z_ans,w_ans))