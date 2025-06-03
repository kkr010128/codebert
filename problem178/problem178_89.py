n = list(map(int,input().split()))
m = []
for i in range(2):
    m.append(n[0])
    n.pop(0)
    
n.append(m[0])
n.append(m[1])
  
print(*n)